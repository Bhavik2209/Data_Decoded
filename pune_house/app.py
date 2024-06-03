# Save this as app.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r'C:\Users\SVI\Desktop\Code_Decoded\pune_house\random_forest_regressor.pkl')

# Title of the app
st.title("House Rent Prediction")

# Function to take user input
def user_input_features():
    house_size = st.number_input("House Size (in sqft)", min_value=0)
    latitude = st.number_input("Latitude")
    longitude = st.number_input("Longitude")
    numBathrooms = st.number_input("Number of Bathrooms", min_value=0)
    numBalconies = st.number_input("Number of Balconies", min_value=0)
    SecurityDeposit = st.number_input("Security Deposit", min_value=0)
    numBalconies_nan = st.checkbox("Number of Balconies is NaN")
    numBathrooms_nan = st.checkbox("Number of Bathrooms is NaN")
    verification_years = st.number_input("Verification Years", min_value=0)
    verification_days = st.number_input("Verification Days", min_value=0)
    verification_months = st.number_input("Verification Months", min_value=0)
    verification_hours = st.number_input("Verification Hours", min_value=0)
    status = st.selectbox("Status", ["Furnished", "Semi-Furnished", "Unfurnished"])
    house_type = st.selectbox("House Type", ["Apartment", "Independent Floor", "Independent House", "Villa"])

    data = {
        'house_size': house_size,
        'latitude': latitude,
        'longitude': longitude,
        'numBathrooms': numBathrooms,
        'numBalconies': numBalconies,
        'SecurityDeposit': SecurityDeposit,
        'numBalconies_nan': int(numBalconies_nan),
        'numBathrooms_nan': int(numBathrooms_nan),
        'verification_years': verification_years,
        'verification_days': verification_days,
        'verification_months': verification_months,
        'verification_hours': verification_hours,
        'Status_Furnished': 1 if status == "Furnished" else 0,
        'Status_Semi-Furnished': 1 if status == "Semi-Furnished" else 0,
        'Status_Unfurnished': 1 if status == "Unfurnished" else 0,
        'house_type_cleaned_Apartment': 1 if house_type == "Apartment" else 0,
        'house_type_cleaned_Independent Floor': 1 if house_type == "Independent Floor" else 0,
        'house_type_cleaned_Independent House': 1 if house_type == "Independent House" else 0,
        'house_type_cleaned_Villa': 1 if house_type == "Villa" else 0
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Show user input data on the sidebar
st.sidebar.header('User Input Parameters')
st.sidebar.write(input_df)

# Prediction
prediction = model.predict(input_df)

# Display prediction
st.subheader('Predicted Rent Price')
st.write(f"{prediction[0]:.2f} Rupees")

