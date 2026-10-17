import pandas as pd

import joblib  # Save and load trained machine-learning objects

from sklearn.model_selection import train_test_split # split data inot training and testing set

from sklearn.preprocessing import OneHotEncoder # Convert categorical data into numeric features

from sklearn.preprocessing import StandardScaler  # Standardize numeric features

from sklearn.compose import ColumnTransformer  # Apply different preprocessing to different columns

from sklearn.linear_model import LogisticRegression  # Classification model for predicting credit risk

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix  # Classification evaluation tools

df = pd.read_csv(
    "german_credit.data",
    sep=r"\s+",
    header=None
)
column_names = [
    "checking_status",       # 0
    "duration",              # 1
    "credit_history",        # 2
    "purpose",               # 3
    "credit_amount",         # 4
    "savings_status",        # 5
    "employment",            # 6
    "installment_rate",      # 7
    "personal_status",       # 8
    "other_debtors",         # 9
    "residence_since",       # 10
    "property",              # 11
    "age",                   # 12
    "other_installments",    # 13
    "housing",               # 14
    "existing_credits",      # 15
    "job",                   # 16
    "dependents",            # 17
    "telephone",             # 18
    "foreign_worker",        # 19
    "credit_risk"            # 20
]

df.columns = column_names  # Replace numbered headings with descriptive names


df["credit_risk"] = df["credit_risk"].map({1: 0, 2: 1}) # convert original labels: good= 0 bad= 1

print(df["credit_risk"].value_counts()) # count good and bad credit outcomes

print(df.head())
print(df.shape)

X = df.drop(columns=["credit_risk"]) # keep all columns except our target

y = df["credit_risk"] # keep only the target labels

print("X shape:", X.shape) # show rows and feature columns
print("y shape:", y.shape) # show number of target labels

X_train, X_test, y_train, y_test = train_test_split(
    X, y,                 # Features and target
    test_size=0.2,        # Reserve 20% for testing
    random_state=42,      # Make the random split reproducible
    stratify=y            # Preserve the 70/30 target distribution
)

print("Training rows:", X_train.shape[0])
print("Testing rows:", X_test.shape[0])

numeric_columns = X.select_dtypes(include=["number"]).columns  # Find numeric feature columns

categorical_columns = X.select_dtypes(include=["str", "object"]).columns  # Select text/category columns explicitly

print("Numeric columns:", numeric_columns.tolist())  # Display numeric column names
print("Categorical columns:", categorical_columns.tolist())  # Display categorical column names

preprocessor = ColumnTransformer(
    transformers=[
        ("categories", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
        ("numbers", StandardScaler(), numeric_columns)  # Scale numeric features using training data
    ]
)

X_train_ready = preprocessor.fit_transform(X_train)  # Learn categories from training data and transform it

X_test_ready = preprocessor.transform(X_test)  # Apply the same transformation to testing data

print("Training features after encoding:", X_train_ready.shape)
print("Testing features after encoding:", X_test_ready.shape)

model = LogisticRegression(max_iter=2000)  # Create the classification model

model.fit(X_train_ready, y_train)  # Train using borrower features and their actual outcomes

print("Model training complete!")  # Confirm training finished

predictions = model.predict(X_test_ready)  # Predict credit risk for the 200 test applicants

print("First 10 predictions:", predictions[:10])  # Display the first 10 predicted outcomes

print("First 10 actual outcomes:", y_test.iloc[:10].to_numpy())  # Display the correct outcomes for comparison

accuracy = accuracy_score(y_test, predictions)  # Compare all 200 predictions with actual outcomes

print("Model accuracy:", accuracy)  # Display accuracy as a decimal

print("Model accuracy percentage:", round(accuracy * 100, 2), "%")  # Convert accuracy to percentage

precision = precision_score(y_test, predictions)  # How often predicted bad-credit cases are actually bad

recall = recall_score(y_test, predictions)  # How many actual bad-credit cases the model identifies

print("Precision:", round(precision * 100, 2), "%")  # Display precision as a percentage

print("Recall:", round(recall * 100, 2), "%")  # Display recall as a percentage

cm = confusion_matrix(y_test, predictions)  # Count correct and incorrect predictions by class

print("Confusion matrix:\n", cm)  # Display the four classification outcomes

joblib.dump(
    {
        "preprocessor": preprocessor,  # Save the fitted encoder and scaler
        "model": model                 # Save the trained classifier
    },
    "credit_risk_model.joblib"
)

print("Model and preprocessor saved successfully!")

saved = joblib.load("credit_risk_model.joblib")  # Reload our saved objects

loaded_preprocessor = saved["preprocessor"]  # Retrieve the fitted encoder and scaler

loaded_model = saved["model"]  # Retrieve the trained classifier

loaded_features = loaded_preprocessor.transform(X_test)  # Prepare the same test data

loaded_predictions = loaded_model.predict(loaded_features)  # Predict using the loaded model

assert (predictions == loaded_predictions).all()  # Confirm every prediction matches

print("Saved model verification PASSED!")