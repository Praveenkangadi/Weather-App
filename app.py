import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.title("🌱 Air Quality Prediction App (India)")

# Load data
data = pd.read_excel("AirQualityUCI.xlsx")
data = data.dropna()

# Define features and target
target = "CO(GT)"
features = [col for col in data.columns if col not in ['Date', 'Time', target]]
X = data[features]
y = data[target]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

st.subheader("Predict Air Quality for a State")

# Dummy input data for a state (user can modify this part)
state_input = [st.number_input(f"Enter value for {feat}", float(X[feat].min()), float(X[feat].max()), float(X[feat].mean())) for feat in features]

if st.button("Predict"):
    prediction = model.predict([state_input])[0]
    if prediction < 2:
        quality = "Good"
    elif prediction < 5:
        quality = "Moderate"
    else:
        quality = "Poor"
    st.success(f"Predicted CO level: {prediction:.2f} => Air Quality: {quality}")
