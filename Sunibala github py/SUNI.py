import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

# NVIDIA client
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)



app = FastAPI(title="Sunibala AI")

# What the frontend will send
class Message(BaseModel):
    user_input: str

@app.get("/")
def home():
    return {"message": "Sunibala AI is running. Go to /docs to test"}

@app.post("/chat")
def chat(msg: Message):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system", 
                "content": "You are Sunibala. You are a B.Tech CSE student, 7th semester at Manipur Technical University, from Phayeng, Manipur. Talk like a friendly student. Be helpful and supportive."
            },
            {"role": "user", "content": msg.user_input}
        ],
        temperature=1,
        top_p=1,
        max_tokens=4096,
        stream=False,
    )
    return {"reply": completion.choices[0].message.content}