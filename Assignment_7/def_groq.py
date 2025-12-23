from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

def call_groq(user_input):
    api_key = os.getenv("groq_api_key")

    chat = ChatGroq(model = "llama-3.3-70b-versatile",api_key=api_key)

    #user_input = input("You : ")

    result = chat.invoke(user_input)

    return result.content

# input  = input("you : ")
# result = call_groq(input)
# print("AI : ",result)