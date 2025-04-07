import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('soil_quality_model.pkl')

# Streamlit app title
st.title("Soil Quality Checker")

# Input fields for soil parameters
pH = st.number_input("Enter pH value:", min_value=0.0, max_value=14.0, step=0.1)
nitrogen = st.number_input("Enter Nitrogen content (mg/kg):", min_value=0.0, step=0.1)
phosphorus = st.number_input("Enter Phosphorus content (mg/kg):", min_value=0.0, step=0.1)
potassium = st.number_input("Enter Potassium content (mg/kg):", min_value=0.0, step=0.1)
organic_carbon = st.number_input("Enter Organic Carbon content (%):", min_value=0.0, step=0.1)

# Predict button
if st.button("Check Soil Quality"):
    # Prepare input data
    input_data = pd.DataFrame([[pH, nitrogen, phosphorus, potassium, organic_carbon]],
                              columns=['pH', 'Nitrogen', 'Phosphorus', 'Potassium', 'Organic_Carbon'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result
    st.success(f"The predicted soil type is: {prediction}")
