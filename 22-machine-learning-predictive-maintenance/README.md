
# Machine Learning Predictive Maintenance

## Project Overview

This project uses machine learning to predict industrial equipment failures based on machine sensor measurements.

The goal is to help manufacturing companies identify potential equipment failures early, prioritize maintenance inspections, and reduce unexpected downtime.

## Business Problem

Unexpected machine failures can cause:

- Production downtime
- Expensive equipment repairs
- Delayed customer orders
- Increased maintenance costs

A predictive maintenance system analyzes historical sensor readings to identify machines that may be at risk of failure.

## Dataset

Dataset: AI4I 2020 Predictive Maintenance Dataset

Source: UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

The dataset contains 10,000 records and 14 original columns.

Target variable:

- `Machine failure`
- `0` = Normal operation
- `1` = Machine failure

Class distribution:

- Normal: 9,661
- Failure: 339

The dataset is imbalanced because failures are relatively rare.

## Machine Learning Features

The model uses five numerical sensor features:

1. Air temperature [K]
2. Process temperature [K]
3. Rotational speed [rpm]
4. Torque [Nm]
5. Tool wear [min]

Failure-mode indicators are excluded to avoid target leakage.

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- Logistic Regression
- StandardScaler
- Joblib
- Git and GitHub

## Machine Learning Workflow

1. Load the manufacturing dataset.
2. Inspect the data and missing values.
3. Select sensor features and the target.
4. Split data into training and testing sets.
5. Standardize numerical features.
6. Train a Logistic Regression model.
7. Predict machine failures.
8. Evaluate predictions using a confusion matrix.
9. Calculate precision, recall, and F1-score.
10. Save the trained pipeline with Joblib.
11. Reload the model and verify its predictions.

The model uses an 80/20 stratified train-test split with `random_state=42`.

The training pipeline combines `StandardScaler` and `LogisticRegression` with `class_weight="balanced"`.

## Model Results

The model was evaluated on 2,000 test records.

### Confusion Matrix

```text
[[1585  347]
 [  11   57]]
```

| Result | Count |
|---|---:|
| True Negatives | 1,585 |
| False Positives | 347 |
| False Negatives | 11 |
| True Positives | 57 |

### Evaluation Metrics

| Metric | Result |
|---|---:|
| Accuracy | 82% |
| Failure Precision | 14% |
| Failure Recall | 84% |
| Failure F1-score | 0.24 |

The model detected 57 of 68 actual machine failures.

However, it also generated 347 false alarms.

The high failure recall is promising, but low precision means the model requires further evaluation and improvement before production deployment.

## Business Interpretation

The model could potentially help factory maintenance teams prioritize equipment inspections.

However, predictions should not automatically trigger machine shutdowns.

Additional evaluation is needed to determine whether the benefits of identifying failures outweigh the costs of false alarms.

## Installation

Clone the portfolio repository and navigate to this project folder.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the required libraries:

```bash
python -m pip install pandas scikit-learn joblib
```

## Running the Project

Make sure `ai4i2020.csv` is located in the project folder.

Run:

```bash
python main.py
```

The program trains the model, evaluates its predictions, and saves the trained pipeline to:

```text
predictive_maintenance_model.joblib
```

## Saved Model Verification

The trained pipeline is saved using Joblib.

The saved model is then loaded and used to generate predictions on the test dataset.

Verification confirmed that all 2,000 predictions from the loaded model matched the original model's predictions.

Only load Joblib model files from trusted sources.

## Future Improvements

- Compare additional classification algorithms.
- Tune classification thresholds to reduce unnecessary alerts.
- Evaluate maintenance costs and missed-failure risks.
- Add automated tests.
- Create a FastAPI prediction endpoint.
- Package the application using Docker.
- Deploy the model using AWS or Microsoft Azure.
- Add production monitoring and model evaluation.

## Project Status

Machine learning development and saved-model verification completed.

Cloud deployment and production integration are planned future improvements.
