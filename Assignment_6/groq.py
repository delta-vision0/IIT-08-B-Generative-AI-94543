import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
def groq_call(prompt):
    API_KEY = os.getenv("groq_api_key")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {API_KEY}"
    }

    data = {
        "model" : "llama-3.3-70b-versatile",
        "messages": [{
            "role":"user",
            "content" : prompt}
        ]
    }

    response = requests.post(url , headers=headers,data=json.dumps(data))
    reply = response.json()["choices"][0]["message"]["content"]
    return reply