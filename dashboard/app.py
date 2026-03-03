import streamlit as st
import pandas as pd
from model.risk_scoring import calculate_risk

st.title("FraudLink AI Dashboard")

file_path = "data/sample_transactions.csv"

risk = calculate_risk(file_path)

st.subheader("Risk Scoring Results")

for account, score in risk.items():
    st.write(f"{account} : {score}")