# Fetch Rewards Backend Engineering Intern Task

Write a program that reads from a CSV file called transactions.csv in the current working directory, processes an argument, and returns a response based on the conditions outlined in the next section

## Background

Our users have points in their accounts. Users only see a single balance in their accounts. But for reporting purposes, we actually track their points per payer. In our system, each transaction record contains: payer (string), points (integer), timestamp (date).

For earning points, it is easy to assign a payer. We know which actions earned the points. And thus, which partner should be paying for the points.
When a user spends points, they don't know or care which payer the points come from. But, our accounting team does care how the points are spent. There are two rules for determining what points to "spend" first:

- We want the oldest points to be spent first (oldest based on transaction timestamp, not the order they’re received)
- We want no payer's points to go negative.

My code will do following tasks:

- Read the transactions from a CSV file.

- Spend points based on the argument using the rules above.

- Return all payer point balances.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python and Pandas
```

### Installing

A step by step series of installation instructions

Downloading

```
Download the main.py file
```

Ensuring files are in same folder

```
Keep the transactions.csv file in the same location
```

## Running the code

To run the program you need to run it using following command:

```
python main.py int_val
```

where: int_vl represents any integer value

**_Input:_** The script takes one command-line argument, an integer representing the amount of points to be spent.

**_Output:_** The program then returns the point balance for each payer after spending the specified points.

## Authors

- **Vatsal S Chheda** - _Initial work_ - [LinkedIn](https://www.linkedin.com/in/vatsalchheda/)
