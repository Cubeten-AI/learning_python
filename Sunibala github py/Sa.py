import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

# 1. Setup NVIDIA client
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY")
)

# 2. Setup FastAPI
app = FastAPI()

# 3. Request body model
class ChatRequest(BaseModel):
    message: str

# 4. API Endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system", 
                "content": "You are Oken. You are a B.Tech CSE student, 7th semester at Manipur Technical University, from Phayeng, Manipur. Be friendly and helpful. If anyone asks who you are, tell them you are Oken from MTU."
            },
            {"role": "user", "content": request.message}
        ],
        temperature=1,
        top_p=1,
        max_tokens=4096,
        stream=False,
    )
    return {"reply": completion.choices[0].message.content}


@app.get("/")
def home():
    return {"message": "Oken AI is running. Use /chat endpoint"}