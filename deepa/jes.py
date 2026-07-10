from google import genai
from google.genai import types
from fastapi import FastAPI

# Gemini Client
client = genai.Client(
    api_key="AQ.Ab8RN6IDg9qN52Z-D1D3Egev5yOk6QFAx0QXeVeDUHYID5-uFA"
)

app = FastAPI()


# Home API
@app.get("/")
def home():
    return {
        "message": "this is deepa api "
    }


# Chat API
@app.post("/chat")
def ai_response(prompt: str):
    response = client.models.generate_content(
        model="gemini-flash-latest",   # Use a valid model
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="""i am deepa from ngaikhong khullen ,i am a btech cse student of manipur technical university ,now i am in 7th semester and i learning ai in cubeten."""
        )
    )

    return {
        "response": response.text
    }