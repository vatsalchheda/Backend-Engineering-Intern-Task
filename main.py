"""
Fetch Rewards Backend Software Engineering Internship Take-Home Test. 
"""

# Imports
import sys
import argparse
import pandas as pd
from collections import defaultdict


def load_data(name):
    df = pd.read_csv(name)
    cols = ['payer', 'points', 'timestamp']
    df = df.drop(columns=[col for col in df.columns if col not in cols])

    try:
        df['points'] = pd.to_numeric(df['points'], errors='coerce').astype(int)
    except Exception as err:
        print('Exception while reading values ::: ' + 'IntConversionError ::: ' + str(err))
        sys.exit()

    
    try:
        if df.isnull().values.any():
            raise ValueError("Data contains Null/NaN/None values")
    except ValueError as ve:
        print('Exception while parsing values. Name: ' + 'NullValueError: ' + str(ve))
        sys.exit()

    return df


def initialize(df):
    points_total = df['points'].sum()
    df = df.sort_values(by=['year', 'month', 'day', 'time'])
    pipeline = df.values.tolist()
    bal = defaultdict(int)
    for t in pipeline:
        bal[t[0]] += t[1]
    
    return (points_total, pipeline, bal)

def preprocess(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%dT%H:%M:%SZ')
    
    try:
        df['time'] = df['timestamp'].dt.time
        df['day'] = df['timestamp'].dt.day
        df['month'] = df['timestamp'].dt.month
        df['year'] = df['timestamp'].dt.year
        df = df.drop(columns=['timestamp'])
    except Exception as err:
        print('Exception while converting values. Name: ' + 'DateTimeError: ' + str(err))
        sys.exit()
    
    return df




def get_answer(points_total, pipeline, bal, points_remaining):
    if points_remaining > points_total:
        print('Exception in passed parameter. Name: WrongParameterError: The user does not have ' + str(points_remaining) + ' in their account.')
        sys.exit()
    elif points_remaining <= 0:
        print('Exception in passed parameter. Name: WrongParameterError: Please input a positive, non-zero integer')
        sys.exit()

    for t in pipeline:
        if points_remaining == 0:
            break

        payer, points = t[0], t[1]
        if points <= points_remaining:
            bal[payer] -= points
            points_remaining -= points
        else:
            bal[payer] -= points_remaining
            points_remaining = 0

    return bal



def main():
    parser = argparse.ArgumentParser(description='This program takes one command line argument')
    parser.add_argument('value', type=int, help='An integer value')
    points_remaining = parser.parse_args().value

    df = load_data('transactions.csv')
    df = preprocess(df)
    points_total, pipeline, bal = initialize(df)
    res = get_answer(points_total, pipeline, bal, points_remaining)

    print(dict(res))


if __name__ == "__main__":
    main()
