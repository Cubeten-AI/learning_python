from google import genai
from google.genai import types
from fastapi import FastAPI
from pydantic import BaseModel
import os

# TODO: move this to .env later
API_KEY = "AQ.Ab8RN6IK5RcRlLofq8VZetiWEgcrwXPrICF8pE5Rg7zcSz3ttA" 
client = genai.Client(api_key=API_KEY)

app = FastAPI(title="Sunibala AI Assistant API")

# This tells FastAPI to expect JSON like: {"prompt": "hi"}
class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Sunibala AI Assistant is running. Go to /docs to test"}

@app.post("/chat")
def ai_response(request: ChatRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=request.prompt,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an AI assistant for Sunibala. "
                "Sunibala is from Phayeng. "
                "She is a Computer Engineering student in 7th semester at MTU. "
                "She is currently pursuing an AI internship at Cube Ten. "
                "She specializes in UI design and development. "
                "Answer in a friendly way."
            )
        )
    )
    return {"response": response.text}