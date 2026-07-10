from google import genai
from google.genai import types
from fastapi import FastAPI

# Gemini Client
client = genai.Client(
    api_key="AQ.Ab8RN6Ilj6DI4lXBAF49mNNtMWZdOCpwG-CN62c8Et4P4Nd-Zg"
)

app = FastAPI()


# Home API
@app.get("/")
def home():
    return {
        "message": "This is Jeshmita ai.py"
    }


# Chat API
@app.post("/chat")
def ai_response(prompt: str):
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",   # Use a valid model
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="""I am Yaikhom Jeshmita Devi, a B.Tech student in the Computer Science and Engineering (CSE) department at Manipur Technical University. I live in Imphal, Manipur, India. I am currently doing an Artificial Intelligence (AI) internship at CubeTen. I am passionate about programming, web development, and learning new technologies. I enjoy building projects using HTML, CSS, JavaScript, Python, and FastAPI, and I am continuously improving my technical and problem-solving skills to prepare for an entry-level IT career."""
        )
    )

    return {
        "response": response.text
    }