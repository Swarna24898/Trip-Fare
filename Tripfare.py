import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('best_gbr_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Trip Fare Predictor", layout="centered")

# App title
st.title("NYC Taxi Fare Predictor")
st.markdown("Enter trip details to predict the total fare amount")

# Input fields
trip_duration = st.number_input("Trip Duration (in minutes)", min_value=0.0, value=10.0, step=0.5)
trip_distance = st.number_input("Trip Distance (in km)", min_value=0.0, value=3.0, step=0.1)
pickup_hour = st.slider("Pickup Hour (0 - 23)", min_value=0, max_value=23, value=12)
is_night = st.radio("Is it Night Time?", ["Yes", "No"])
fare_per_km = st.number_input("Fare per KM", min_value=0.0, value=5.0, step=0.1)

# Convert categorical input
is_night_value = 1 if is_night == "Yes" else 0

# Predict button
if st.button("Predict Fare"):
    input_data = np.array([[trip_duration, trip_distance, pickup_hour, is_night_value, fare_per_km]])
    
    try:
        prediction = model.predict(input_data)
        st.success(f"Predicted Total Fare Amount: ${prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
