from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import os
from langchain.tools import tool
from dotenv import load_dotenv
import streamlit as st
import requests
from langchain_core.messages import HumanMessage
import json
load_dotenv()
if "messages" not in st.session_state:
    st.session_state.messages = []
@tool
def get_weather(city_name):
    """
This get_weather() function gets the current weather of given city.
    If weather cannot be found, it returns 'Error'.
    This function doesn't return historic or general weather of the city.

    :param city: str input - city name
    :returns current weather in json format or 'Error' 
"""
    api_key = os.getenv("api_key")
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
        return str(weather_info)
    else:
        return None

# @wrap_model

@tool
def calculator(expression):
    """
    This calculator() function gets any methamatical expression and solves it carefully,
    it is the best way to handle any type of mathematical expression , or even simple maths 
    so that the output answer will be 100% correct !
    everytime you use this tool say : according to calculator tool ...
"""
    try:    
        result = eval(expression)
        return str(result)
    except:
        return "error , it cannot be resolved"
    
@tool
def file_reader(filepath):
    """
    this tool can be used to get information from a file,
    the data inside file can be read using this function , this is very important function to get the information about file
    if filepath not found you should give not found message instead of big errors
    """
    try:    
        with open (filepath , 'r') as file:
            file_info = file.read()
            return file_info
    except:
        return "File Not Found , is it really there ?"
llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider= "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("groq_api_key")
)
agent = create_agent(model=llm,
                tools =[get_weather,calculator,file_reader],
                system_prompt="you are a helpful assistant"
                )
user_input = st.chat_input("Enter Your msg : ")
if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages":st.session_state.messages})
    st.session_state.messages = result["messages"]


    # if user_input:
    #     st.session_state.messages_groq.append({
    #         "role": "user",
    #         "content": user_input
    #     })
    #     response = ai_msg.content
    #     st.session_state.messages_groq.append({
    #         "role": "assistant",
    #         "content": response
    #     })

    for msg in st.session_state.messages:
        if msg.type in ("human", "ai") and msg.content.strip():
            st.chat_message(msg.type).write(msg.content)
    #     st.chat_message(msg["role"]).write(msg["content"])
    # # ("AI : ",ai_msg.content)
    # st.session_state.messages = result["messages"]
