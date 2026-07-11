from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import List
import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from openai import OpenAI

# 1. NVIDIA API configuration
BASE_URL = "https://integrate.api.nvidia.com/v1"
API_KEY =( "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")  # Put your newly generated key here!

# 2. Setup FastAPI
app = FastAPI(title="Nexus AI API - NVIDIA Powered")
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Data Models for Memory
class PastMessage(BaseModel):
    role: str
    text: str

class ChatMessage(BaseModel):
    prompt: str
    history: List[PastMessage]

# 4. The Main Chat Route
@app.post('/chat')
def ai_response(message: ChatMessage):
    try:
        now = datetime.now()
        current_time_string = now.strftime("%A, %B %d, %Y at %I:%M %p")
        
        # --- BUILD THE MESSAGE ARRAY ---
        # OpenAI/NVIDIA expects a list of dictionaries, starting with the system prompt
        messages_array = [
            {
                "role": "system", 
                "content": f"You are Nexus, a premium AI assistant. The user you are talking to is named Vedant. Always be helpful, friendly, and concise. The current date and time is {current_time_string} .My iam name is vedant iam originally fom malom tulihal mainipur ,iam a software engineer and iam studying b.tech in a university called MTU(Maniput Technical University). I am a very good person and i love to help people. I am very friendly and i love to make new friends. I am very concious about my work and i always try to do my best. I am very passionate about my work and i always try to learn new things. I am very creative and i always try to think out of the box. I am very positive and i always try to see the good in people. I am very humble and i always try to be kind to everyone. I am very honest and i always try to be truthful. I am very loyal and i always try to be faithful. I am very responsible and i always try to be accountable. I am very respectful and i always try to be polite. I am very patient and i always try to be understanding. I am very generous and i always try to be giving. I am very compassionate and i always try to be empathetic. I am very courageous and i always try to be brave. I am very determined and i always try to be persistent. I am very disciplined and i always try to be self-controlled. I am very focused and i always try to be attentive. I am very organized and i always try to be systematic. I am very resourceful and i always try to be innovative. I am very adaptable and i always try to be flexible. I am very resilient and i always try to be strong."
            }
        ]

        # Add the chat history to the array so the AI remembers the context
        if message.history:
            for msg in message.history:
                # Map our frontend roles ('User'/'AI') to OpenAI's required roles ('user'/'assistant')
                role = "user" if msg.role == "User" else "assistant"
                messages_array.append({"role": role, "content": msg.text})
        
        # Finally, add the newest message you just typed in the UI
        messages_array.append({"role": "user", "content": message.prompt})

        # --- CALL THE NVIDIA API ---
        completion = client.chat.completions.create(
          model="openai/gpt-oss-120b",
          messages=messages_array,
          temperature=0.7,
          max_tokens=1024,
          stream=False,
        )
        
        # Extract the text from the API response object
        ai_reply = completion.choices[0].message.content
        return {"reply": ai_reply}
        
    except Exception as e:
        return {"reply": f"An error occurred: {str(e)}"}