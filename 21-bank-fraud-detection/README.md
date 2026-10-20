# Bank Fraud Detection — Machine Learning

## 1. Project Overview

This project is a machine-learning fraud detection system built with Python and scikit-learn.

It analyzes credit card transaction data, trains a Logistic Regression model, and estimates the probability that a transaction is fraudulent.

The system flags suspicious transactions for further review.

## 2. Business Problem

Banks process large numbers of transactions every day. Fraudulent transactions can cause financial losses, while incorrectly flagging legitimate transactions can inconvenience customers.

The goal of this project is to:

- Identify potentially fraudulent transactions.
- Reduce the number of missed fraud cases.
- Balance fraud detection against false alarms.
- Estimate the financial impact of different detection thresholds.
- Provide a reusable prediction function.

## 3. Technologies Used

- Python
- pandas — Data loading and analysis
- NumPy — Numerical operations
- Matplotlib — Data visualization
- scikit-learn — Machine learning and evaluation
- Logistic Regression — Fraud classification
- StandardScaler — Feature scaling
- joblib — Model persistence
- pytest — Automated testing
- Git and GitHub — Version control

## 4. Dataset

This project uses the Credit Card Fraud Detection dataset, originally provided by the Machine Learning Group at Université Libre de Bruxelles and available through Kaggle.

Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset contains:

- 284,807 transactions
- 284,315 legitimate transactions
- 492 fraudulent transactions

The dataset is highly imbalanced because fraudulent transactions are rare.

The original CSV is excluded from GitHub due to its size.

Download the dataset separately and place `creditcard.csv` inside the project directory to run the training script.

## 5. Machine Learning Workflow

1. Load the credit card transaction dataset.
2. Explore the data and identify class imbalance.
3. Visualize legitimate and fraudulent transactions.
4. Separate features (`X`) from labels (`y`).
5. Split the dataset into training and testing sets.
6. Scale features using StandardScaler.
7. Train a Logistic Regression classifier.
8. Evaluate predictions using classification metrics.
9. Analyze the confusion matrix.
10. Adjust the fraud detection threshold.
11. Estimate the business costs of false alarms and missed fraud.
12. Save and reload the trained model.
13. Build a reusable prediction function.
14. Validate the prediction interface with pytest.

## 6. Model Evaluation

The model is evaluated using:

- Precision
- Recall
- F1-score
- Classification report
- Confusion matrix

Because fraud is rare, accuracy alone is not sufficient to evaluate performance.

A model could achieve high accuracy by predicting that almost every transaction is legitimate while missing actual fraud.

This project focuses on understanding false positives and false negatives.

## 7. Fraud Detection Threshold

The prediction interface uses a fraud probability threshold of 70%.

Transactions with predicted fraud probabilities greater than or equal to 0.70 are flagged for review.

This threshold is a project-specific decision, not a universal banking standard.

The probabilities are model-generated scores and have not been independently calibrated.

## 8. Business Cost Analysis

The project uses hypothetical costs to compare detection thresholds:

- False alarm: $10
- Missed fraudulent transaction: $500

On the held-out test set:

| Metric | 50% Threshold | 70% Threshold |
|---|---:|---:|
| True negatives | 55,478 | 56,219 |
| False positives | 1,386 | 645 |
| False negatives | 8 | 9 |
| True positives | 90 | 89 |
| Estimated cost | $17,860 | $10,950 |

Under these assumptions, the 70% threshold reduces estimated costs by $6,910 compared with the 50% threshold.

These figures are illustrative, not actual bank losses or guaranteed future performance.

## 9. Project Files

```text
21-bank-fraud-detection/
├── main.py
├── predict.py
├── test_predict.py
├── fraud_model.joblib
├── requirements.txt
├── README.md
└── .gitignore
```

The original dataset is downloaded separately and excluded from version control.

## 10. Installation

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## 11. Running the Project

To train and evaluate the fraud detection model:

```bash
python main.py
```

The script displays a transaction distribution chart, trains the model, evaluates its predictions, and saves the trained pipeline.

To use the saved model for a sample prediction:

```bash
python predict.py
```

The prediction script loads the saved model and evaluates one transaction from the local dataset.

It does not retrain the model.

## 12. Automated Testing

Run the tests with:

```bash
python -m pytest test_predict.py -v
```

The current test suite checks that:

- The prediction function is callable.
- The fraud probability is between 0 and 1.
- The fraud decision follows the configured 70% threshold.

The latest local test run completed with two passing tests.

## 13. Limitations and Future Improvements

This is an educational portfolio project, not a production banking system.

Potential improvements include:

- Comparing Logistic Regression with other classifiers.
- Calibrating fraud probabilities.
- Evaluating performance on newer, unseen transaction data.
- Adding cross-validation and threshold selection using validation data.
- Creating a FastAPI prediction endpoint.
- Adding input validation and stronger automated tests.
- Monitoring model performance and data drift.
- Improving security, logging, and deployment processes.

## 14. Skills Demonstrated

This project demonstrates hands-on experience with:

- Supervised machine learning
- Binary classification
- Data exploration and visualization
- Imbalanced datasets
- Feature scaling
- Model training and evaluation
- Classification thresholds
- Business cost analysis
- Model serialization
- Reusable Python functions
- Automated testing
- Dependency management
- Technical documentation
- Git and GitHub

## 15. Project Summary

Built a Python-based credit card fraud detection system using scikit-learn and Logistic Regression.

Implemented data preprocessing, model evaluation, threshold-based fraud review decisions, hypothetical business cost comparisons, model persistence, and automated tests.

The project demonstrates how machine-learning predictions can support business decisions while accounting for the trade-off between missed fraud and false alarms.
