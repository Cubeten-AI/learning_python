import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

# NVIDIA client
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

app = FastAPI(title="Sunibala AI")

class Message(BaseModel):
    user_input: str

# 1. HOME PAGE WITH UI
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sunibala AI</title>
        <style>
            body { font-family: Arial; background: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; }
           .chatbox { width: 400px; height: 600px; background: white; border-radius: 10px; box-shadow: 0 0 10px #ccc; display: flex; flex-direction: column; }
           .header { background: #6a5acd; color: white; padding: 15px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold; }
           .messages { flex: 1; padding: 15px; overflow-y: auto; }
           .msg { margin-bottom: 10px; padding: 8px 12px; border-radius: 15px; max-width: 80%; }
           .user { background: #DCF8C6; margin-left: auto; }
           .bot { background: #E8E8E8; margin-right: auto; }
           .input-area { display: flex; padding: 10px; border-top: 1px solid #ddd; }
            input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 20px; }
            button { padding: 10px 15px; margin-left: 5px; border: none; background: #6a5acd; color: white; border-radius: 20px; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="chatbox">
            <div class="header">Sunibala AI - B.Tech CSE, MTU</div>
            <div class="messages" id="messages"></div>
            <div class="input-area">
                <input type="text" id="userInput" placeholder="Ask Sunibala anything..." onkeypress="if(event.key==='Enter') sendMessage()">
                <button onclick="sendMessage()">Send</button>
            </div>
        </div>

        <script>
            async function sendMessage() {
                const input = document.getElementById('userInput');
                const messages = document.getElementById('messages');
                const userText = input.value;
                if (userText.trim() === '') return;

                messages.innerHTML += `<div class="msg user">${userText}</div>`;
                input.value = '';

                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({user_input: userText})
                });
                const data = await res.json();
                messages.innerHTML += `<div class="msg bot">${data.reply}</div>`;
                messages.scrollTop = messages.scrollHeight;
            }
        </script>
    </body>
    </html>
    """

# 2. CHAT API
@app.post("/chat")
def chat(msg: Message):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system", 
                "content": "You are Sunibala. You are a B.Tech CSE student, 7th semester at Manipur Technical University, from Phayeng, Manipur. Talk like a friendly student. Be helpful and supportive. Keep answers short and conversational."
            },
            {"role": "user", "content": msg.user_input}
        ],
        temperature=0.8,
        max_tokens=500,
        stream=False,
    )
    return {"reply": completion.choices[0].message.content}