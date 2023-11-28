import streamlit as st
import requests

st.markdown("DON'T BE SCAMMED 💰")
st.markdown("TAXI PRICE PREDICTOR 🚕")


pickup_datetime = st.text_input("pickup datetime", value="2012-10-06 12:10:20")
pickup_longitude = st.number_input("pickup longitude", value=40.7614327)
pickup_latitude = st.number_input("pickup latitude", value=-73.9798156)
dropoff_longitude = st.number_input("dropoff longitude", value=40.6513111)
dropoff_latitude = st.number_input("dropoff latitude", value=-73.8803331)
passenger_count = st.number_input("Number of passengers", value=2)

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count,
}

url = 'https://taxifare.lewagon.ai/predict'

if st.button('Fare Price'):
    response = requests.get(url, params=params).json()
    fare = float("{:.2f}".format(response["fare"]))
    f"Your fare is: ${fare}"
