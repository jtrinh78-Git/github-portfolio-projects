
# Section 1 - Imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# Section 2 - Load Customer Data
df = pd.read_excel("data/Online Retail.xlsx")
print(df.head())


# Section 3 - Inspect Dataset Size
print("Dataset shape:", df.shape)


# Section 4 - Check Missing Values
print(df.isnull().sum())


# Section 5 - Remove Missing Customer IDs
df = df.dropna(subset=["CustomerID"])
print("Cleaned dataset shape:", df.shape)


# Section 6 - Inspect Invalid Transactions
print("Negative or zero quantities:", (df["Quantity"] <= 0).sum())
print("Negative or zero prices:", (df["UnitPrice"] <= 0).sum())


# Section 7 - Keep Valid Purchases
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
print("Valid purchase rows:", df.shape)


# Section 8 - Calculate Purchase Value
df = df.copy()
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
print(df[["Quantity", "UnitPrice", "TotalPrice"]].head())


# Section 9 - Calculate Total Spending Per Customer
customer_spending = df.groupby("CustomerID")["TotalPrice"].sum()
print(customer_spending.head())


# Section 10 - Count Purchases Per Customer
customer_frequency = df.groupby("CustomerID")["InvoiceNo"].nunique()
print(customer_frequency.head())


# Section 11 - Find Each Customer's Latest Purchase
customer_last_purchase = df.groupby("CustomerID")["InvoiceDate"].max()
print(customer_last_purchase.head())


# Section 12 - Find the Dataset's Latest Date
latest_date = df["InvoiceDate"].max()
print("Latest transaction date:", latest_date)


# Section 13 - Calculate Customer Recency
customer_recency = (latest_date - customer_last_purchase).dt.days
print(customer_recency.head())


# Section 14 - Combine RFM Measurements
rfm = pd.DataFrame({
    "Recency": customer_recency,
    "Frequency": customer_frequency,
    "Monetary": customer_spending
})

print(rfm.head())


# Section 20 - Inspect Monetary Distribution
print(rfm["Monetary"].describe())


# Section 22 - Prepare RFM for Log Transformation
rfm_log = rfm.copy()

rfm_log["Frequency"] = np.log1p(rfm_log["Frequency"])
rfm_log["Monetary"] = np.log1p(rfm_log["Monetary"])

print(rfm_log.head())


# Section 16 - Create the Feature Scaler
scaler = StandardScaler()


# Section 17 - Scale the RFM Measurements
rfm_scaled = scaler.fit_transform(rfm_log)
print(rfm_scaled[:5])


# Section 18 - Verify Scaled Data Shape
print("Scaled data shape:", rfm_scaled.shape)

# Section 24 - Create K-Means Model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Section 25 - Train the K-Means Model
kmeans.fit(rfm_scaled)

print("K-Means training completed!")

# Section 26 - Inspect Customer Cluster Labels
print("Customer cluster labels:", kmeans.labels_[:10])

# Section 27 - Assign Clusters to Customers
rfm["Cluster"] = kmeans.labels_

print(rfm.head())

# Section 28 - Summarize Customer Clusters
cluster_summary = rfm.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean()

print(cluster_summary)

# Section 29 - Count Customers in Each Cluster
cluster_counts = rfm["Cluster"].value_counts().sort_index()

print("Customers per cluster:")
print(cluster_counts)

# Section 31 - Evaluate Cluster Quality
score = silhouette_score(rfm_scaled, kmeans.labels_)

print("Silhouette Score:", score)

# Section 32 - Compare Cluster Counts
for k in range(2, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(rfm_scaled)

    test_score = silhouette_score(rfm_scaled, model.labels_)
    print("Clusters:", k, "Score:", round(test_score, 4))

# Section 33 - Name Customer Segments
segment_names = {
    0: "Occasional Customers",
    1: "High-Value Frequent Customers",
    2: "Inactive Customers"
}

rfm["Segment"] = rfm["Cluster"].map(segment_names)

print(rfm[["Cluster", "Segment"]].head())


# Section 34 - Export Customer Segmentation Report
rfm.to_csv("customer_segments.csv")

print("Customer segmentation report saved!")


# Section 35 - Verify Exported Customer Report
report = pd.read_csv("customer_segments.csv")

print("Exported report shape:", report.shape)
print(report.head())

# Section 36 — Install Streamlit - python -m pip install streamlit

# Section 37 - Customer Segmentation Dashboard
import streamlit as st
import pandas as pd

st.title("Customer Segmentation Dashboard")

df = pd.read_csv("customer_segments.csv")

st.write("Customer Segmentation Results")
st.dataframe(df)