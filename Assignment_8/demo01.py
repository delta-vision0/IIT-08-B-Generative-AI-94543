from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
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
llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider= "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("groq_api_key")
)
conversation = []
agent = create_agent(model=llm,
                tools =[],
                system_prompt="you are a helpful assistant"
                )
while True:
    user_input = input("Enter Your msg : ")
    conversation.append({"role" : "user" , "content" : user_input})
    result = agent.invoke({"messages":conversation})
    ai_msg = result["messages"][-1]
    print("AI : ",ai_msg.content)
    conversation = result["messages"]
