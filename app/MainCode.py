import os
import requests
import chainlit as cl

OLLAMA_API_BASE = os.getenv('OLLAMA_API_BASE', 'http://localhost:11434')

@cl.on_message
async def main(message: str):
    # Prepare the request to Ollama API
    url = f"{OLLAMA_API_BASE}/api/generate"
    data = {
        "model": "mxbai",
        "prompt": message,
        "stream": False
    }

    # Make the API call
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        await cl.Message(content=result['response']).send()
    else:
        await cl.Message(content=f"Error: Unable to get response from Ollama API. Status code: {response.status_code}").send()

@cl.on_chat_start
def start():
    cl.Message(content="Hello! How can I assist you today?").send()