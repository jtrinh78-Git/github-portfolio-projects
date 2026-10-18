# Section 37 - Customer Segmentation Dashboard
import streamlit as st
import pandas as pd

st.title("Customer Segmentation Dashboard")

df = pd.read_csv("customer_segments.csv")

# Section 38 - Display Total Customers
total_customers = len(df)

st.metric("Total Customers", f"{total_customers:,}")

# Section 39 - Customer Segment Chart
segment_counts = df["Segment"].value_counts()

# Section 40 - Business Summary
st.subheader("Customer Segment Summary")

segment_summary = df.groupby("Segment")[
    ["Recency", "Frequency", "Monetary"]
].mean().round(2)

st.dataframe(segment_summary)

st.subheader("Customers by Segment")
st.bar_chart(segment_counts)

st.write("Customer Segmentation Results")
st.dataframe(df)

# Section 41 - Download Customer Report
st.download_button(
    label="Download Customer Report",
    data=df.to_csv(index=False),
    file_name="customer_segments.csv",
    mime="text/csv"
)