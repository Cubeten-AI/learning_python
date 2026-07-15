from fastapi import FastAPI, HTTPException
from google import genai
from google.genai import types

client = genai.Client(api_key="AQ.Ab8RN6I66oB8mJEXTIEcQ6y1hZXjThIyIgiZuGCPJGruS_WccA")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Gemini AI API is running"}

@app.get("/chat")
def ai_response(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful assistant that explains complex topics simply."
            )
        )
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))