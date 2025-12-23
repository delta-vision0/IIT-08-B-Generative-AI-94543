import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
def gemini_call(prompt):
    API_KEY = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"
    flag = True
    while flag:
        if prompt == "exit":
            flag = False
        else:
            headers = {
                "Content-Type": "application/json"
            }

            data = {"contents":[{"parts": [{"text": prompt}]}]}

            reponse = requests.post(url, headers=headers, json=data)

            reply = reponse.json()

            gemini_reply = reply["candidates"][0]["content"]["parts"][0]["text"]
            return gemini_reply