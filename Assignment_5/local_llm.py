import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
def local_call(prompt):
    API_KEY = os.getenv("groq_api_key")
    url = "http://127.0.0.1:1234/v1/chat/completions"
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer"
    }

    data = {
        "model" : "google/gemma-3-4b",
        "messages": [{
            "role":"user",
            "content" : prompt}
        ]
    }

    response = requests.post(url , headers=headers,data=json.dumps(data))
    reply = response.json()["choices"][0]["message"]["content"]
    return reply
