import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('placement_prediction_1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit App Title
st.title("Linear Regression Model Deployment")

# User Input
st.write("Enter the values for prediction:")
input_value = st.number_input("Enter a numeric value:", min_value=0.0, max_value=10.0, step=0.1)

# Make Prediction
if st.button("Predict"):
    input_array = np.array([[input_value]])  # Reshape input for model
    prediction = model.predict(input_array)
    st.write(f"Predicted Output: {prediction[0]:.2f} LPA")

# Run this script using: streamlit run app.py
