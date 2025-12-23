import streamlit as st
import requests
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
            "Wind Speed": data["wind"]["speed"],
            "Data" : data
        }
        return weather_info
    else:
        return None