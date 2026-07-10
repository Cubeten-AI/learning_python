from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(
    title="Deepa AI Assistant",
    version="1.0"
)

# NVIDIA OpenAI Client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)


# Request Model
class ChatRequest(BaseModel):
    prompt: str


# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to Deepa AI Assistant API"
    }


# Chat API
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Deepa's assistant. "
                        "If anyone asks about Deepa, answer based on the following information:\n"
                        "- Deepa is from Ngaikhong Khullen, Bishnupur.\n"
                        "- She is studying B.Tech CSE at Manipur Technical University (MTU).\n"
                        "- She is learning AI at Cubeten."
                    ),
                },
                {
                    "role": "user",
                    "content": request.prompt,
                },
            ],
            temperature=1,
            top_p=1,
            max_tokens=4096,
        )

        return {
            "response": completion.choices[0].message.content
        }

    except Exception as e:
        return {
            "error": str(e)
        }