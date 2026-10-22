import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("ai4i2020.csv")
print(df.head())
print(df.columns)
print(df["Machine failure"].value_counts())
print(df.isnull().sum())

X = df[["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"]]

y = df["Machine failure"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(X_train.shape)

model = make_pipeline(StandardScaler(), LogisticRegression(
    max_iter=1000, class_weight="balanced"
))

model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions[:10])
print(pd.Series(predictions).value_counts())
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions, zero_division=0))

joblib.dump(model, "predictive_maintenance_model.joblib")

loaded_model = joblib.load("predictive_maintenance_model.joblib")

loaded_predictions = loaded_model.predict(X_test)

print((predictions == loaded_predictions).all())