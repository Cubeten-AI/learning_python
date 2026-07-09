from google import genai
from google.genai import types
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# TODO: move API key to .env file later
client = genai.Client(api_key="AQ_AQ8RWL0QeJeK51BnI8uTezQoWoTnoPZJodyY1lQQLDLuf9XSx")

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

# HTML UI inside Python
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sunibala AI Assistant</title>
    <style>
        body { font-family: 'Segoe UI'; background: linear-gradient(135deg, #ff6b9d, #c44569); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .chat-box { background: white; width: 700px; height: 85vh; border-radius: 20px; padding: 20px; display: flex; flex-direction: column; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }
        .header { text-align: center; background: #ff6b9d; color: white; padding: 15px; border-radius: 15px; margin-bottom: 15px; }
        #messages { flex: 1; overflow-y: auto; border: 1px solid #ddd; padding: 15px; border-radius: 10px; background: #fff8fa; }
        .user { text-align: right; background: #ff6b9d; color: white; padding: 10px 14px; border-radius: 15px; margin: 8px 0 8px 30%; }
        .ai { text-align: left; background: #eee; color: #333; padding: 10px 14px; border-radius: 15px; margin: 8px 30% 8px 0; }
        .input-area { display: flex; margin-top: 15px; gap: 10px; }
        input { flex: 1; padding: 12px; border-radius: 20px; border: 2px solid #ddd; outline: none; }
        button { padding: 12px 22px; border-radius: 20px; border: none; background: #ff6b9d; color: white; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="chat-box">
        <div class="header">
            <h2>🤖 Sunibala AI Assistant</h2>
            <small>She's from Phayeng | CSE Student MTU 7th Sem | AI Intern @ Cube Ten, Mantripukhri</small>
        </div>
        <div id="messages"><div class="ai">Hi! I'm Sunibala's AI assistant. Ask me anything 😊</div></div>
        <div class="input-area">
            <input id="prompt" placeholder="Type message..." onkeypress="if(event.key==='Enter') send()">
            <button onclick="send()">Send</button>
        </div>
    </div>
<script>
async function send() {
    let msg = document.getElementById('prompt').value;
    if(!msg) return;
    let chatbox = document.getElementById('messages');
    chatbox.innerHTML += `<div class="user">${msg}</div>`;
    document.getElementById('prompt').value = '';
    
    let res = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({prompt: msg})
    });
    let data = await res.json();
    chatbox.innerHTML += `<div class="ai">${data.response}</div>`;
    chatbox.scrollTop = chatbox.scrollHeight;
}
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE

@app.post("/chat")
def ai_response(request: ChatRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=request.prompt,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an AI assistant for Sunibala. "
                "She's from Phayeng. "
                "She is a CSE student of MTU 7th sem. "
                "She has done AI internship from Cube Ten, Mantripukhri. "
                "She specializes in UI design and development. "
                "Answer in a friendly and helpful way."
            )
        )
    )
    return {"response": response.text}