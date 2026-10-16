# Project 19 — Credit Risk Classification

## Overview

An educational machine-learning project that predicts credit-risk categories using the German Credit dataset from the UCI Machine Learning Repository.

Built with Python, Pandas, and scikit-learn.

## Dataset

- Source: [UCI Statlog (German Credit Data)](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data)
- 1,000 credit applicants
- 20 input features
- Original labels: 1 = good credit, 2 = bad credit
- Converted labels: 0 = good credit, 1 = bad credit

## Machine-Learning Workflow

1. Load and inspect the dataset with Pandas.
2. Separate features (`X`) and labels (`y`).
3. Split the dataset into 80% training and 20% testing, preserving class proportions.
4. Encode categorical features with `OneHotEncoder`.
5. Standardize numeric features with `StandardScaler`.
6. Train a Logistic Regression classifier.
7. Evaluate predictions on the held-out test set.
8. Save and reload the trained model and preprocessor using Joblib.
9. Verify that reloaded predictions match the original predictions.

## Results

| Metric | Result |
|---|---:|
| Accuracy | 78.00% |
| Precision (bad-credit class) | 66.67% |
| Recall (bad-credit class) | 53.33% |
| Majority-class baseline accuracy | 70.00% |

Confusion matrix:

```text
[[124  16]
 [ 28  32]]
```

The model correctly classified 156 of 200 test applicants. However, it missed 28 of the 60 applicants labeled as bad credit.

## How to Run

Create and activate a Python virtual environment, then install dependencies:

```bash
python -m pip install -r requirements.txt
python real_data.py
```

The script trains, evaluates, saves, and reloads the model.

## Project Files

- `real_data.py` — Real-dataset training and evaluation
- `main.py` — Small Pandas practice example
- `practice.py` — Additional Pandas practice
- `german_credit.data` — German Credit dataset
- `requirements.txt` — Python dependencies

## Limitations

This project is for education and portfolio demonstration only. It is not validated for real lending or credit approval decisions.

The dataset is historical, model recall is limited, and fairness, calibration, generalization, and regulatory compliance have not been established.