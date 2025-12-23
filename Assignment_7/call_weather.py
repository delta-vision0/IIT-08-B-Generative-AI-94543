import weather as w
import streamlit as st
import os
from dotenv import load_dotenv
import def_groq as groq
import json
load_dotenv()

st.title("Weather App AI ")
city = st.text_input("Enter city name:")
api_key = os.getenv("api_key")
if city:
    weather_info = w.get_weather(city, api_key)
    if weather_info:
        st.write(f"Temperature: {weather_info['Temperature']}°C")
        st.write(f"Humidity: {weather_info['Humidity']}%")
        st.write(f"Description: {weather_info['Description']}")
        st.write(f"Wind Speed: {weather_info['Wind Speed']} m/s")
        if(weather_info['Temperature'] < 10):
            st.snow()  # Add snow effect

        llm_input = {
  "task": "explain_weather",
  "weather_data": weather_info["Data"],
  "output_spec": {
    "language": "english",
    "tone": "neutral_professional",
    "length": "brief",
    "format": {
      "type": "fixed_bulleted_sections",
      "sections": [
          {
          "title": "Here is the weather report for the requested location:"
        },
        {
          "title": "Location",
          "instruction": "State the city or location name only."
        },
        {
          "title": "Temperature Summary",
          "instruction": "Summarize current temperature and feels-like temperature if available."
        },
        {
          "title": "Conditions",
          "instruction": "Describe sky condition, humidity, and wind briefly."
        },
        {
          "title": "Additional Notes",
          "instruction": "Mention any notable weather detail, or write 'None'."
        }
      ]
    }
  },
  "rules": {
    "use_only_provided_data": True,
    "no_forecast": True,
    "no_advice": True,
    "no_assumptions": True,
    "no_extra_sections": True
  }
}

        prompt = json.dumps(llm_input , indent=2)

        result =  groq.call_groq(prompt)
        st.write(result)


    else:
        st.write("City not found.")
else:
    st.write("Please enter a city name.")

    