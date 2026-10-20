from predict import predict_fraud
import pandas as pd



def test_predict_fraud_is_callable():
    assert callable(predict_fraud)


def test_fraud_probability_is_valid():
    sample = pd.read_csv("creditcard.csv", nrows=1)
    transaction = sample.drop(columns=["Class"]).iloc[0].to_dict()
    is_fraud, probability = predict_fraud(transaction)
    assert 0.0 <= probability <= 1.0
    assert is_fraud == (probability >= 0.70)
    