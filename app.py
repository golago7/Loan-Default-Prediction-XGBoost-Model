import streamlit as st
import numpy as np
import pickle

# Load the trained model from the pickle file
with open("xgboost_model.sav", "rb") as file:
    model = pickle.load(file)

# Define a function to make predictions
def predict_loan_default(features):
    prediction = model.predict(features)
    return prediction

# Streamlit app
def main():
    st.title("Loan Default Predictor")
    st.write("This app predicts whether the customer will default.")
    
    # User input form
    with st.form("loan_form"):
        st.header("Enter Loan Application Information")
        
        # Input fields for loan application details
        loan_amnt = st.text_input("Loan Amount ($) Applied by Applicant")
        loan_term = st.selectbox("Loan Term", ("3 Years", "5 Years"))
        interest_rate = st.text_input("Interest Rate (%)")
        loan_grade = st.selectbox("Loan Grade", ("A", "B", "C", "D", "E", "F", "G"))
        loan_subgrade = st.selectbox("Loan Subgrade", ('B2', 'C1', 'A4', 'C4', 'A2', 'C2', 'B4', 'A5', 'E2', 'B5', 'A3',
                                                       'C5', 'E5', 'B1', 'D5', 'D4', 'E3', 'B3', 'C3', 'D3', 'A1', 'F5',
                                                       'E1', 'E4', 'F3', 'D1', 'G3', 'F2', 'D2', 'F4', 'F1', 'G1', 'G5', 'G2', 'G4'))
        job_experience = st.selectbox("Years of Job Experience", ('<5 Years', '10+ years', '6-10 years'))
        home_ownership = st.selectbox("Home Ownership Status", ('OWN', 'MORTGAGE', 'RENT', 'NONE', 'OTHER'))
        annual_income = st.text_input("Annual Income ($)")
        income_verification_status = st.selectbox("Income Verification Status", ('Not Verified', 'Verified', 'Source Verified'))
        loan_purpose = st.selectbox("Purpose of the Loan", ('debt_consolidation', 'credit_card', 'other', 'home_improvement'))
        state_code = st.selectbox("State Code", ('NC', 'SC', 'TX', 'MO', 'IL', 'NY', 'CT', 'CA', 'VA', 'GA', 'OR', 'NV', 'LA', 'RI', 'IN', 
                                                 'AZ', 'OK', 'MN', 'WY', 'HI', 'MI', 'CO', 'MS', 'NJ', 'WA', 'UT', 'NM', 'KY', 'MA', 'FL', 
                                                 'PA', 'WI', 'OH', 'DE', 'DC', 'WV', 'MD', 'TN', 'NE', 'AL', 'KS', 'SD', 'VT', 'MT', 'AK', 
                                                 'AR', 'NH', 'ME', 'ND', 'ID'))
        debt_to_income = st.text_input("Debt-to-Income Ratio")
        delinq_2yrs = st.text_input("Number of Delinquencies in Last 2 Years")
        public_records = st.text_input("Public Records on File")
        revolving_balance = st.text_input("Revolving Balance ($)")
        total_acc = st.text_input("Total Accounts")
        interest_receive = st.text_input("Interest Received ($)")
        application_type = st.selectbox("Application Type", ('INDIVIDUAL', 'JOINT'))
        last_week_pay = st.text_input("Last Week's Pay")
        total_current_balance = st.text_input("Total Current Balance ($)")
        total_revolving_limit = st.text_input("Total Revolving Credit Limit ($)")
       
        # Submit button
        submitted = st.form_submit_button("Predict Loan Default")

        # When the form is submitted
        if submitted:
            try:
                # Prepare the feature array (convert inputs to appropriate types)
                features = np.array([[float(loan_amnt), loan_term, float(interest_rate), loan_grade, loan_subgrade, job_experience, 
                                      home_ownership, float(annual_income), income_verification_status, loan_purpose, state_code, 
                                      float(debt_to_income), int(delinq_2yrs), int(public_records), float(revolving_balance), 
                                      int(total_acc), float(interest_receive), application_type, float(last_week_pay), 
                                      float(total_current_balance), float(total_revolving_limit)]])
                
                # Predict Loan Default Status
                default = predict_loan_default(features)
                
                # Display the prediction result
                st.success(f"The customer will: {'default' if default[0] else 'not default'}")
            
            except ValueError:
                st.error("Please enter valid numerical values for all the inputs.")

if __name__ == "__main__":
    main()
