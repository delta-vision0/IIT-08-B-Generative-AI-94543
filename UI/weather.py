import streamlit as st
import requests
import json 
import os
from dotenv import load_dotenv
load_dotenv()


def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Description": data["weather"][0]["description"],
            "Wind Speed": data["wind"]["speed"]
        }
        return weather_info
    else:
        return None

st.title("Weather App")
city = st.text_input("Enter city name:")
api_key = os.getenv("api_key")
if city:
    weather_info = get_weather(city, api_key)
    if weather_info:
        st.write(f"Temperature: {weather_info['Temperature']}°C")
        st.write(f"Humidity: {weather_info['Humidity']}%")
        st.write(f"Description: {weather_info['Description']}")
        st.write(f"Wind Speed: {weather_info['Wind Speed']} m/s")
        st.snow()  # Add snow effect
    else:
        st.write("City not found.")
else:
    st.write("Please enter a city name.")
