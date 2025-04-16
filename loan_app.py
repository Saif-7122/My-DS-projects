import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('loan_approval_model.pkl')

# Streamlit app interface
st.title('Loan Approval Prediction')
st.write("Enter the details to predict loan approval:")

# Inputs from user
gender = st.selectbox("Gender", ['Male', 'Female'])
married = st.selectbox("Marital Status", ['Married', 'Single'])
dependents = st.selectbox("Number of Dependents", ['0', '1', '2', '3+'])
self_employed = st.selectbox("Self Employed", ['No', 'Yes'])
loan_amount = st.number_input("Loan Amount", min_value=1000, max_value=1000000)
loan_term = st.selectbox("Loan Term (in years)", ['10', '15', '20', '25'])
credit_history = st.selectbox("Credit History", ['1', '0'])

# Prepare input for prediction (transform categorical data to numbers if needed)
input_data = np.array([[gender, married, dependents, self_employed, loan_amount, loan_term, credit_history]])

# Convert inputs (this depends on how you processed the data during training)
# For example, encode 'Male' to 1, 'Female' to 0 if you did that in training.

# Prediction when the button is pressed
if st.button('Predict Loan Approval'):
    # Prediction logic here
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Loan Approved!")
    else:
        st.error("Loan Denied!")

