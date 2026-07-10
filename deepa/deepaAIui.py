from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI(
    title="Deepa AI Assistant",
    version="1.0"
)

# NVIDIA Client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)


# Home Page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deepa AI Assistant</title>
        <style>
            body{
                font-family:Arial,sans-serif;
                background:#f5f5f5;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
            }

            .container{
                width:600px;
                background:white;
                padding:20px;
                border-radius:10px;
                box-shadow:0 0 10px rgba(0,0,0,0.2);
            }

            h2{
                text-align:center;
                color:#333;
            }

            textarea{
                width:100%;
                height:120px;
                padding:10px;
                font-size:16px;
            }

            button{
                width:100%;
                margin-top:15px;
                padding:10px;
                background:#007bff;
                color:white;
                border:none;
                border-radius:5px;
                cursor:pointer;
                font-size:16px;
            }

            button:hover{
                background:#0056b3;
            }
        </style>
    </head>

    <body>

    <div class="container">

        <h2>🤖 Deepa AI Assistant</h2>

        <form action="/chat" method="post">

            <textarea
                name="prompt"
                placeholder="Ask something..."
                required
            ></textarea>

            <button type="submit">
                Send
            </button>

        </form>

    </div>

    </body>
    </html>
    """


# Chat Page
@app.post("/chat", response_class=HTMLResponse)
def chat(prompt: str = Form(...)):
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Deepa's assistant. "
                        "If anyone asks about Deepa, answer based on the following information:\n"
                        "- Deepa is from Ngaikhong Khullen, Bishnupur.\n"
                        "- She is studying B.Tech CSE at Manipur Technical University (MTU).\n"
                        "- She is learning AI at Cubeten."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=1,
            top_p=1,
            max_tokens=4096,
        )

        answer = completion.choices[0].message.content

    except Exception as e:
        answer = f"Error: {str(e)}"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deepa AI Assistant</title>

        <style>
            body{{
                font-family:Arial,sans-serif;
                background:#f5f5f5;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
            }}

            .container{{
                width:700px;
                background:white;
                padding:20px;
                border-radius:10px;
                box-shadow:0 0 10px rgba(0,0,0,.2);
            }}

            textarea{{
                width:100%;
                height:120px;
                padding:10px;
                font-size:16px;
            }}

            button{{
                width:100%;
                padding:10px;
                margin-top:15px;
                background:#007bff;
                color:white;
                border:none;
                border-radius:5px;
                cursor:pointer;
            }}

            .response{{
                margin-top:20px;
                padding:15px;
                background:#eef5ff;
                border-left:5px solid #007bff;
                border-radius:5px;
                white-space:pre-wrap;
            }}
        </style>

    </head>

    <body>

    <div class="container">

        <h2>🤖 Deepa AI Assistant</h2>

        <form action="/chat" method="post">

            <textarea name="prompt">{prompt}</textarea>

            <button type="submit">
                Send
            </button>

        </form>

        <div class="response">
            <h3>Response</h3>
            <p>{answer}</p>
        </div>

    </div>

    </body>
    </html>
    """