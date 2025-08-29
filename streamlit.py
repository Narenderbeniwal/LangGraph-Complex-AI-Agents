import streamlit as st
import pandas as pd

# Load the Excel file (sheet names should be: 'Customer Information', 'Alerts Table')
excel_file = "customer_data.xlsx"

# Read the sheets into DataFrames
customer_df = pd.read_excel(excel_file, sheet_name='Customer Information')
alerts_df = pd.read_excel(excel_file, sheet_name='Alerts Table')

# Create tabs
tabs = st.tabs(["Customer Information", "KYC Table", "Customer Transaction Information", "Alerts Table"])

# Customer ID filter
selected_customer_id = st.selectbox(
    "Select Customer ID to filter:",
    customer_df["customer_id"].unique()
)

# Apply filter for all DataFrames
filtered_customer_df = customer_df[customer_df["customer_id"] == selected_customer_id]
filtered_alerts_df = alerts_df[alerts_df["customer_id"] == selected_customer_id]

with tabs[0]:
    st.header("Customer Information")
    st.dataframe(filtered_customer_df)

with tabs[1]:
    st.header("KYC Table")
    st.write("Add your KYC Table data here.")

with tabs[2]:
    st.header("Customer Transaction Information")
    st.write("Add your Customer Transaction Information data here.")

with tabs[3]:
    st.header("Alerts Table")
    st.dataframe(filtered_alerts_df)
