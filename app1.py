import streamlit as st
import joblib

# Load the trained model
model = joblib.load("Package_Prediction.pkl")  # Ensure you have a trained model saved as 'model.pkl'

# Streamlit UI
st.title("CGPA to Package Prediction")
st.write("Enter your CGPA to predict the expected package")

cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.01)

if st.button("Predict"):
    prediction = model.predict([[cgpa]])[0]
    st.success(f"Predicted Package: {prediction:.2f} LPA")


