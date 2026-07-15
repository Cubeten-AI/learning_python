from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google import genai
from google.genai import types

app = FastAPI(title="Jeshmita AI")

# Gemini Client
client = genai.Client(
    api_key="AQ.Ab8RN6Ilj6DI4lXBAF49mNNtMWZdOCpwG-CN62c8Et4P4Nd-Zg"
)


# ---------------- HOME PAGE ----------------

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Jeshmita AI</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:#f5f5f5;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}

.container{
    width:800px;
    background:white;
    border-radius:15px;
    box-shadow:0 0 20px rgba(0,0,0,.15);
    overflow:hidden;
}

.header{
    background:#1a73e8;
    color:white;
    text-align:center;
    padding:20px;
    font-size:30px;
    font-weight:bold;
}

.chat{
    height:450px;
    overflow-y:auto;
    padding:20px;
    background:#fafafa;
}

.user{
    background:#1a73e8;
    color:white;
    padding:12px;
    border-radius:10px;
    margin:10px 0;
    text-align:right;
}

.ai{
    background:#e9ecef;
    padding:12px;
    border-radius:10px;
    margin:10px 0;
}

.footer{
    display:flex;
    padding:15px;
    gap:10px;
}

input{
    flex:1;
    padding:15px;
    font-size:18px;
}

button{
    width:120px;
    background:#1a73e8;
    color:white;
    border:none;
    border-radius:8px;
    font-size:18px;
    cursor:pointer;
}

button:hover{
    background:#0f5dd7;
}

</style>

</head>

<body>

<div class="container">

<div class="header">
🤖 Jeshmita AI
</div>

<div class="chat" id="chat"></div>

<div class="footer">

<input
id="prompt"
placeholder="Ask anything..."
onkeydown="if(event.key==='Enter') sendMessage()"
/>

<button onclick="sendMessage()">
Send
</button>

</div>

</div>

<script>

async function sendMessage(){

    let prompt=document.getElementById("prompt").value.trim();

    if(prompt==="") return;

    let chat=document.getElementById("chat");

    chat.innerHTML += `
        <div class="user">${prompt}</div>
    `;

    document.getElementById("prompt").value="";

    chat.innerHTML += `
        <div class="ai" id="loading">
            Thinking...
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;

    try{

        const response = await fetch(
            "/chat?prompt=" + encodeURIComponent(prompt),
            {
                method:"POST"
            }
        );

        const data = await response.json();

        document.getElementById("loading").remove();

        if(data.error){
            chat.innerHTML += `
                <div class="ai">
                    ❌ ${data.error}
                </div>
            `;
        }else{
            chat.innerHTML += `
                <div class="ai">
                    ${data.response}
                </div>
            `;
        }

        chat.scrollTop = chat.scrollHeight;

    }catch(error){

        document.getElementById("loading").remove();

        chat.innerHTML += `
            <div class="ai">
                Something went wrong.
            </div>
        `;
    }

}

</script>

</body>
</html>
"""


# ---------------- CHAT API ----------------

@app.post("/chat")
def ai_response(prompt: str):

    try:

        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="""
You are Jeshmita AI, the personal AI assistant of Yaikhom Jeshmita Devi.

Your purpose is to assist users by providing helpful, accurate, and friendly responses while representing Jeshmita professionally.

"""
            )
        )

        return {
            "response": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }