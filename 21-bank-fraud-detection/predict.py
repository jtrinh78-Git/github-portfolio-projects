import joblib
import pandas as pd
from pathlib import Path


model = joblib.load("fraud_model.joblib")

def predict_fraud(transaction):
    transaction_df = pd.DataFrame([transaction])
    fraud_probability = model.predict_proba(transaction_df)[0][1]
    is_fraud = fraud_probability >= 0.70
    return is_fraud, fraud_probability

if __name__ == "__main__":
    sample_data = pd.read_csv(Path(__file__).with_name("creditcard.csv"), nrows=1)
    transaction = sample_data.drop(columns=["Class"]).iloc[0].to_dict()
    is_fraud, fraud_probability = predict_fraud(transaction)
    print("Flagged for fraud review:", is_fraud)
    print("Fraud probability:", fraud_probability)