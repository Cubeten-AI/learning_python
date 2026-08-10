from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import chromadb
import os
from dotenv import load_dotenv

# Find .env in the parent folder
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(env_path)

print("API KEY FOUND:", os.getenv("NVIDIA_API_KEY") is not None)

app = Flask(__name__)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)
chroma_client = chromadb.PersistentClient(path="../chroma_db")

collection = chroma_client.get_or_create_collection("gift_magi")

@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data["question"]

    print("Question:", question)

    # Create embedding for question
    query = client.embeddings.create(
    input=[question],
    model="nvidia/nv-embed-v1",
    encoding_format="float",
    extra_body={
        "input_type": "query",
        "truncate": "NONE"
    }
)

    query_vector = query.data[0].embedding


    # Search ChromaDB
    results = collection.query(

        query_embeddings=[query_vector],

        n_results=4

    )


    # Get relevant story sections
    context = "\n".join(results["documents"][0])


    # Send context + question to AI
    messages = [

        {
            "role": "system",

            "content":
            "You are a cheerful AI storyteller. "
            "If the user greets you, greet them back cheerfully. "
            "Answer only from the provided context. "
            "If the answer is not found, politely say "
            "'I couldn't find that in the story.'"
        },

        {
            "role": "user",

            "content": f"""
Context:

{context}

Question:

{question}
"""
        }

    ]


    # Ask GPT
    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    temperature=1,
    top_p=1,
    max_tokens=300,
    stream=False
)


    answer = completion.choices[0].message.content


    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)