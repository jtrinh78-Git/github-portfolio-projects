# Project 20 — Customer Segmentation

## Business Problem

An online retail business wants to understand customer
purchasing behavior so it can identify valuable,
occasional, and inactive customers.

## Solution

Built a Python machine learning application that
analyzes historical retail transactions and groups
customers using K-Means clustering.

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- Streamlit
- Git and GitHub

## Machine Learning Workflow

1. Load retail transaction data.
2. Remove missing customer IDs and invalid purchases.
3. Calculate Recency, Frequency, and Monetary (RFM).
4. Transform and scale customer features.
5. Train a K-Means clustering model.
6. Evaluate clusters using silhouette scores.
7. Assign customer segment labels.
8. Export results to CSV.
9. Display results in a Streamlit dashboard.

## Results

- Analyzed 4,338 customers.
- Identified three customer segments.
- Achieved a silhouette score of approximately 0.416.
- Generated a customer segmentation CSV report.
- Built an interactive dashboard.

## Run the Project

Create and activate a Python virtual environment.

Install dependencies:

pip install -r requirements.txt

Download the UCI Online Retail dataset:

https://archive.ics.uci.edu/dataset/352/online+retail

Place Online Retail.xlsx inside the data folder.

Run the machine learning application:

python main.py

Launch the dashboard:

python -m streamlit run dashboard.py

## Limitations

The dataset contains historical transactions from
2010–2011. Customer recency is calculated relative
to the latest transaction in that dataset.

Customer segment names are descriptive interpretations
of the clusters, not guaranteed classifications.
