import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

df = pd.read_csv("creditcard.csv")

print(df.head())

print(df["Class"].value_counts())

fraud_counts = df["Class"].value_counts()

bars =plt.bar(["Legitimate", "Fraud"], [fraud_counts[0], fraud_counts[1]])

plt.bar_label(bars)

plt.title("Credit Card Fraud Detection")

plt.ylabel("Number of Transactions")

plt.show()

X = df.drop("Class", axis=1)

y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000, class_weight="balanced")
)

model.fit(X_train, y_train)

joblib.dump(model, "fraud_model.joblib")

loaded_model = joblib.load("fraud_model.joblib")

print("Saved model verified:", np.array_equal(model.predict(X_test), loaded_model.predict(X_test)))

print("Model training completed successfully!")

y_pred = model.predict(X_test)

fraud_probabilities = model.predict_proba(X_test)[:, 1]

threshold = 0.70

threshold_predictions = (fraud_probabilities >= threshold).astype(int)

print(confusion_matrix(y_test, threshold_predictions))

false_alarm_cost = 10
missed_fraud_cost = 500

tn, fp, fn, tp = confusion_matrix(y_test, threshold_predictions).ravel()

total_cost = (fp * false_alarm_cost) + (fn * missed_fraud_cost)
print("Estimated bank cost:", total_cost)

print(classification_report(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))