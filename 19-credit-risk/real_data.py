
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Dataset schema from the UCI Statlog German Credit dataset.
COLUMN_NAMES = [
    "checking_status",
    "duration",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_status",
    "employment",
    "installment_rate",
    "personal_status",
    "other_debtors",
    "residence_since",
    "property",
    "age",
    "other_installments",
    "housing",
    "existing_credits",
    "job",
    "dependents",
    "telephone",
    "foreign_worker",
    "credit_risk",
]


def main():
    df = pd.read_csv(
        "german_credit.data",
        sep=r"\s+",
        header=None,
        names=COLUMN_NAMES,
    )

    # Original labels: 1 = good credit, 2 = bad credit.
    # Map bad credit to the positive class for evaluation.
    df["credit_risk"] = df["credit_risk"].map({1: 0, 2: 1})

    print("Target distribution:")
    print(df["credit_risk"].value_counts())
    print("Dataset shape:", df.shape)

    X = df.drop(columns=["credit_risk"])
    y = df["credit_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    numeric_columns = X.select_dtypes(
        include=["number"]
    ).columns

    categorical_columns = X.select_dtypes(
        include=["str", "object"]
    ).columns

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categories",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_columns,
            ),
            (
                "numbers",
                StandardScaler(),
                numeric_columns,
            ),
        ]
    )

    # Fit preprocessing only on training data to prevent data leakage.
    X_train_ready = preprocessor.fit_transform(X_train)
    X_test_ready = preprocessor.transform(X_test)

    model = LogisticRegression(max_iter=2000)
    model.fit(X_train_ready, y_train)

    predictions = model.predict(X_test_ready)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)

    print("\nModel Evaluation")
    print("----------------")
    print(f"Accuracy:  {accuracy:.2%}")
    print(f"Precision: {precision:.2%}")
    print(f"Recall:    {recall:.2%}")
    print("Confusion matrix:")
    print(cm)

    model_path = "credit_risk_model.joblib"

    joblib.dump(
        {
            "preprocessor": preprocessor,
            "model": model,
        },
        model_path,
    )

    # Verify that the persisted model produces identical predictions.
    saved = joblib.load(model_path)

    loaded_features = saved["preprocessor"].transform(X_test)
    loaded_predictions = saved["model"].predict(loaded_features)

    assert (predictions == loaded_predictions).all()

    print("\nSaved model verification PASSED!")


if __name__ == "__main__":
    main()
