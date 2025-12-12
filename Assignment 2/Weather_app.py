import requests
import json
api_key = "d9499a8e176d914b2d80b8a1cb3ef59c"
city_name = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Temperature:",data["main"]["temp"])
    print("Humidity:",data["main"]["humidity"])
    print("Description:",data["weather"][0]["description"])
    print("Wind Speed:",data["wind"]["speed"])
else:
    print("City not found.")