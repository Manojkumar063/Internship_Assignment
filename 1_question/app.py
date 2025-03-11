import streamlit as st
import pandas as pd
import random
import uuid
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")

# Streamlit UI
st.title("Blockchain Fraud Detection System")

# Input fields
amount = st.number_input("Transaction Amount (ETH)", min_value=0.001, max_value=100.0, value=10.0)
gas_fee = st.number_input("Gas Fee (ETH)", min_value=0.0001, max_value=0.1, value=0.01)
tx_count = st.number_input("Transaction Count", min_value=1, max_value=200, value=10)

# Prediction button
if st.button("Detect Fraud"):
    features = [[amount, gas_fee, tx_count]]
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate.")
