from google import genai
from google.genai import types

client = genai.Client(api_key="AQ.Ab8RN6KmUbSC4vryRLASfVcftGzvGMCWPyEn6XTLsIO6EUfV9w")
from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
def ai_response(prompt: str):
    response=client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instructions="You are a helpful assistant that explains complex topics in simple terms.",
        )
    )
    return response.text