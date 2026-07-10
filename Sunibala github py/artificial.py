from google import genai
from google.genai import types
from fastapi import FastAPI

# Gemini Client
client = genai.Client(
    api_key="AQ.Ab8RN6IK5RcRlLofq8VZetiWEgcrwXPrICF8pE5Rg7zcSz3ttA"
)

app = FastAPI()

# Home API
@app.get("/")
def home():
    return {
        "message": "This is Sunibala ai.py"
    }

# Chat API
@app.post("/chat")
def ai_response(prompt: str):
    response = client.models.generate_content(
        model="gemini-flash-latest",   # Use a valid model
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="""I am Sunibala, a B.Tech student in the Computer Science and Engineering (CSE) department at Manipur Technical University. I am from Phayeng, Manipur, India. I am currently in 7th semester. I have done an Artificial Intelligence (AI) internship at CubeTen, Mantripukhri. I am passionate about programming, UI design, web development, and learning new technologies. I enjoy building projects using HTML, CSS, JavaScript, Python, and FastAPI, and I am continuously improving my technical and problem-solving skills to prepare for an entry-level IT career."""
        )
    )

    return {
        "response": response.text
    }