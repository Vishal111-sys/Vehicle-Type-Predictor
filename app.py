
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model pipeline
try:
    model = joblib.load('xgboost_vehicle_type_model.pkl')
except FileNotFoundError:
    st.error("Error: Model file 'xgboost_vehicle_type_model.pkl' not found.")
    st.stop()

# Define constants used in feature engineering (must match training code)
CURRENT_YEAR = 2024
RATE_BINS = [0, 50, 80, 130, np.inf]
RATE_LABELS = ['Budget', 'Standard', 'Premium', 'Luxury']

# ... (Paste the ENTIRE 'make_prediction' function and the Streamlit App Interface code here) ...

# NOTE: Since the app code is very long, please ensure you copy the complete code 
# from the previous response and paste it between the triple quotes below!
