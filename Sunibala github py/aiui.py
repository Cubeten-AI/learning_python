from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google import genai
from google.genai import types

app = FastAPI()

client = genai.Client(
    api_key="AQ.Ab8RN6JYR7nRKgVOupzjb_jqV8AWpp_VWkNWGa1RjvcwDA1PQw"
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Sunibala AI</title>

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
    background:#ff6b9d;
    color:white;
    text-align:center;
    padding:20px;
    font-size:30px;
    font-weight:bold;
}

.header small{
    display:block;
    font-size:14px;
    font-weight:normal;
    margin-top:5px;
    opacity:0.9;
}

.chat{
    height:450px;
    overflow-y:auto;
    padding:20px;
    background:#fff8fa;
}

.user{
    background:#ff6b9d;
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
    border:2px solid #ddd;
    border-radius:8px;
    outline:none;
}

input:focus{
    border-color:#ff6b9d;
}

button{
    width:120px;
    background:#ff6b9d;
    color:white;
    border:none;
    border-radius:8px;
    font-size:18px;
    cursor:pointer;
}

button:hover{
    background:#e05587;
}

</style>

</head>

<body>

<div class="container">

<div class="header">
🤖 Sunibala AI
<small>From Phayeng | CSE 7th Sem MTU | AI Intern @ Cube Ten, Mantripukhri</small>
</div>

<div class="chat" id="chat"></div>

<div class="footer">

<input
id="prompt"
placeholder="Ask anything about Sunibala..."
onkeydown="if(event.key==='Enter') sendMessage()"
/>

<button onclick="sendMessage()">
Send
</button>

</div>

</div>

<script>

async function sendMessage(){

let prompt=document.getElementById("prompt").value;

if(prompt=="") return;

let chat=document.getElementById("chat");

chat.innerHTML+=`
<div class="user">${prompt}</div>
`;

document.getElementById("prompt").value="";

chat.innerHTML+=`
<div class="ai" id="loading">
Thinking...
</div>
`;

chat.scrollTop=chat.scrollHeight;

const response=await fetch(
"/chat?prompt="+encodeURIComponent(prompt),
{
method:"POST"
});

const data=await response.json();

document.getElementById("loading").remove();

chat.innerHTML+=`
<div class="ai">${data.response}</div>
`;

chat.scrollTop=chat.scrollHeight;

}

</script>

</body>
</html>
"""

@app.post("/chat")
def chat(prompt: str):

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="""
You are Sunibala. 
She is from Phayeng, Manipur.
She is a B.Tech CSE student, 7th semester at Manipur Technical University.
She has done an AI internship at CubeTen, Mantripukhri.
She specializes in UI design, web development, HTML, CSS, JavaScript, Python and FastAPI.
Answer in a friendly and helpful tone.
"""
        )
    )

    return {
        "response": response.text
    }