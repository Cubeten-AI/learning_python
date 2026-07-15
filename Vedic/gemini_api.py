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
API_KEY = "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"  # Put your newly generated key here!

# 2. Setup FastAPI
app = FastAPI(title="VEDIC AI - NVIDIA Powered")
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
                "content": (
                    f"You are an AI assistant. The user you are talking to is named VEDIC. "
                    f"He is currently pursuing a B.Tech course at Manipur Technical University in Computer Science Engineering. "
                    f"He is currently an intern at Cubeten, Mantripukhri for AI/ML, working on developing model projects. "
                    f"Always be helpful, friendly, and concise. The current date and time is {current_time_string}."
                )
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