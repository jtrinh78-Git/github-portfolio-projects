# PROJECT 19 — CREDIT RISK MACHINE LEARNING
# SECTION 1 — IMPORT LIBRARIES

import pandas as pd  # Import Pandas for working with tables and datasets

from sklearn.model_selection import train_test_split  # Import the function used to split training and testing data


# SECTION 2 — CREATE OUR PRACTICE DATASET

data = {  # Dictionary containing our borrower information
    "income": [40000, 80000, 55000],  # Annual income for each borrower
    "loan_amount": [20000, None, 30000],  # Loan amounts; None means missing data
    "default": [1, 0, 1]  # Target labels: 1 = defaulted, 0 = did not default
}

df = pd.DataFrame(data)  # Convert our dictionary into a Pandas DataFrame


# SECTION 3 — INSPECT OUR DATASET

print(df)  # Print the entire DataFrame

print(df["income"])  # Print only the income column

print(df.head())  # Print the first 5 rows by default; head(2) prints 2 rows

print(df.shape)  # Show dimensions: (number of rows, number of columns)

df.info()  # Show column names, data types, and non-null counts


# SECTION 4 — FIND MISSING VALUES

print(df.isnull().sum())  # Count missing values in each column


# SECTION 5 — CLEAN MISSING VALUES

df["loan_amount"] = df["loan_amount"].fillna(
    df["loan_amount"].median()  # Calculate median loan amount and use it to fill missing values
)

print(df.isnull().sum())  # Check missing values again after cleaning


# SECTION 6 — TEST OUR DATA CLEANING

assert df.isnull().sum().sum() == 0  # Verify total missing values equal zero; raise an error if false

print("Data cleaning test passed!")  # Print confirmation if the assertion passes


# SECTION 7 — EXPLORE DATA STATISTICS

print(df.describe())  # Show count, mean, std, min, 25%, median (50%), 75%, and max


# SECTION 8 — SEPARATE FEATURES AND TARGET

X = df[["income", "loan_amount"]]  # Features: information used to predict defaults

y = df["default"]  # Target: actual default outcomes (1 or 0)


# SECTION 9 — DISPLAY FEATURES AND TARGET

print(X)  # Print the feature columns

print(y)  # Print the target labels


# SECTION 10 — CHECK DATA DIMENSIONS

print("X shape:", X.shape)  # Show (borrowers, feature columns)

print("y shape:", y.shape)  # Show the number of target values in a one-dimensional Series


# SECTION 11 — CHECK TARGET DISTRIBUTION

print("Target distribution:")  # Print a heading

print(y.value_counts())  # Count how many borrowers defaulted (1) versus did not default (0)