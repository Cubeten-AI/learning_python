from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

# ---------------- HOME PAGE ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Jeshmita Assistant</title>
    <style>
        body{
            font-family:Arial,sans-serif;
            background:#f4f4f4;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            margin:0;
        }

        .container{
            width:500px;
            background:white;
            padding:20px;
            border-radius:12px;
            box-shadow:0 0 15px rgba(0,0,0,.2);
        }

        h2{
            text-align:center;
            color:#2563eb;
        }

        textarea{
            width:100%;
            height:100px;
            padding:10px;
            font-size:16px;
            border-radius:8px;
        }

        button{
            width:100%;
            padding:12px;
            margin-top:10px;
            border:none;
            background:#2563eb;
            color:white;
            font-size:16px;
            border-radius:8px;
            cursor:pointer;
        }

        button:hover{
            background:#1d4ed8;
        }

        #response{
            margin-top:20px;
            background:#eef2ff;
            padding:15px;
            border-radius:8px;
            min-height:100px;
            white-space:pre-wrap;
        }
    </style>
</head>

<body>

<div class="container">

<h2>🤖 Jeshmita Assistant</h2>

<textarea id="prompt" placeholder="Ask me anything..."></textarea>

<button onclick="chat()">Send</button>

<div id="response">Response will appear here...</div>

</div>

<script>
async function chat(){

    const prompt=document.getElementById("prompt").value;

    const res=await fetch("/chat?prompt="+encodeURIComponent(prompt),{
        method:"POST"
    });

    const data=await res.json();

    document.getElementById("response").innerText=data.response;
}
</script>

</body>
</html>
"""

# ---------------- CHAT API ----------------
@app.post("/chat")
def chat(prompt: str):

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role":"system",
                "content":
                "You are Jeshmita Assistant. If anyone asks about Jeshmita, reply with relevant information. Jeshmita is an AI Intern at Cubeten Technologies, and she is from Manipur, India. For all other questions, answer like a helpful AI assistant."
            },
            {
                "role":"user",
                "content":prompt
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