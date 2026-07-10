from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

@app.get("/")
def home():
    return {"message": "Welcome to Jeshmita Assistant API"}

@app.post("/chat")
def chat(prompt: str):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Jeshmita Assistant. "
                    "If anyone asks about Jeshmita, reply with relevant information. "
                    "Jeshmita is an AI Intern at Cubeten Technologies, and she is from Manipur, India. "
                    "For questions unrelated to Jeshmita, act as a helpful AI assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        top_p=1,
        max_tokens=4096,
        stream=False,
    )

    return {
        "response": completion.choices[0].message.content
    }