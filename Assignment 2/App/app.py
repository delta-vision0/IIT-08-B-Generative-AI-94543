import requests
import json
import time
import random
import sys

MODEL_NAME = 'gemini-2.5-flash-preview-09-2025'
API_KEY = "AIzaSyBNUMsMiRs8_mc51QKCZtZqAC2GVxYFjvA"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
API_URL = f"{BASE_URL}/models/{MODEL_NAME}:generateContent?key={API_KEY}"
MAX_RETRIES = 5

def generate_response(history):
    conversation_context = [
        {
            "role": msg["role"], 
            "parts": [{"text": msg["text"]}]
        } 
        for msg in history
    ]

    payload = {
        "contents": conversation_context,
    }

    # Implement exponential backoff for robustness
    for i in range(MAX_RETRIES):
        try:
            # Make the API request
            response = requests.post(
                API_URL, 
                headers={'Content-Type': 'application/json'}, 
                data=json.dumps(payload)
            )

            # Check for HTTP errors
            response.raise_for_status()

            result = response.json()
            
            # Extract the generated text
            if 'candidates' in result and len(result['candidates']) > 0:
                text = result['candidates'][0].get('content', {}).get('parts', [{}])[0].get('text')
                if text:
                    return text
                else:
                    return "Sorry, I couldn't generate a valid text response."
            
            # If successful but no text found, break the retry loop
            return "The model returned an empty response."

        except requests.exceptions.RequestException as e:
            # Handle request exceptions (network issues, rate limiting, bad status codes)
            if i == MAX_RETRIES - 1:
                print(f"Error: API call failed after {MAX_RETRIES} retries. {e}", file=sys.stderr)
                return "Apologies, I'm having trouble connecting right now."
            
            # Calculate delay with jitter
            delay = (2 ** i) + random.uniform(0, 1)
            # print(f"Retrying in {delay:.2f} seconds...", file=sys.stderr)
            time.sleep(delay)
            
    return "An unexpected error occurred during API communication."

def main():
    """
    Runs the main console chatbot loop.
    """
    print("--- Gemini Console Chatbot ---")
    print("Type 'exit' or 'quit' to end the session.")
    print("-" * 30)

    # Stores the conversation history for context (role: 'user' or 'model')
    chat_history = [] 

    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            print("\nExiting chat.")
            break
        except KeyboardInterrupt:
            print("\nExiting chat.")
            break

        if user_input.lower() in ('quit', 'exit'):
            print("Goodbye!")
            break

        if not user_input.strip():
            continue

        # 1. Add user message to history
        chat_history.append({"role": "user", "text": user_input})

        print("Gemini: ... (thinking) ...", end='\r')

        # 2. Get response from the model
        model_response = generate_response(chat_history)
        
        # Clear the thinking message
        print(" " * 30, end='\r') 

        # 3. Print response
        print(f"Gemini: {model_response}")

        # 4. Add model response to history
        chat_history.append({"role": "model", "text": model_response})

if __name__ == "__main__":
    main()