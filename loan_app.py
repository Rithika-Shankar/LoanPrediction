import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


model = joblib.load('loan_model.pkl')

st.set_page_config(page_title="Loan Prediction App", layout="centered")

st.title("Loan Approval Prediction")
st.write("Fill in the details below to predict loan eligibility.")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ['Male', 'Female'])
    married = st.selectbox("Married", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", ['0', '1', '2', '3+'])
    education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Yes', 'No'])

with col2:
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
    loan_amount_term = st.number_input("Loan Term (in days)", min_value=0)
    credit_history = st.selectbox("Credit History", ['1', '0'])
    property_area = st.selectbox("Property Area", ['Urban', 'Semiurban', 'Rural'])

def encode_input():
    gender_val = 1 if gender == 'Male' else 0
    married_val = 1 if married == 'Yes' else 0
    dependents_val = {'0': 0, '1': 1, '2': 2, '3+': 3}[dependents]
    education_val = 1 if education == 'Graduate' else 0
    self_employed_val = 1 if self_employed == 'Yes' else 0
    credit_history_val = int(credit_history)
    property_area_val = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}[property_area]

    return np.array([[gender_val, married_val, dependents_val, education_val, self_employed_val,
                      applicant_income, coapplicant_income, loan_amount, loan_amount_term,
                      credit_history_val, property_area_val]])

if st.button("Predict Loan Status"):
    input_data = encode_input()
    prediction = model.predict(input_data)[0]
    result = "Loan Approved" if prediction == 1 else "Loan Not Approved"

    st.markdown("---")
    st.subheader("Prediction Result")
    st.success(result if prediction == 1 else f"{result}")
    st.markdown("---")
