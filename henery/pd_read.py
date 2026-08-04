from openai import OpenAI
import chromadb
import os
from pypdf import PdfReader
from dotenv import load_dotenv

# ----------------------------
# NVIDIA OpenAI Client
# ----------------------------
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("new_key")
    
    
)

# ----------------------------
# ChromaDB
# ----------------------------
chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="documents"
)


# ----------------------------
# Text Chunking
# ----------------------------
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start += chunk_size - overlap

    return chunks


# ----------------------------
# Read TXT File
# ----------------------------






reader = PdfReader("bishops.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
document = page.extract_text()

chunks = chunk_text(document)


# ----------------------------
# Generate Embeddings
# ----------------------------
embeddings = []

for chunk in chunks:
    response = client.embeddings.create(
        input=[chunk],
        model="nvidia/nv-embed-v1",
        encoding_format="float",
        extra_body={
            "input_type": "passage",
            "truncate": "NONE"
        }
    )

    embeddings.append(response.data[0].embedding)


# ----------------------------
# Store in ChromaDB
# ----------------------------
ids = [f"chunk_{i}" for i in range(len(chunks))]

collection.upsert(
    ids=ids,
    documents=chunks,
    embeddings=embeddings
)

print(f"Stored {len(chunks)} chunks in ChromaDB.")


  

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. "
            "Use the retrieved context to answer the user's question. "
            "If the answer is not in the context, say you don't know."
        )
    }
]

while True:
    query = input("\nYou: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Assistant: Goodbye!")
        break

    # ----------------------------
    # Embed User Query
    # ----------------------------
    query_embedding = client.embeddings.create(
        input=[query],
        model="nvidia/nv-embed-v1",
        encoding_format="float",
        extra_body={
            "input_type": "query",
            "truncate": "NONE"
        }
    )

    query_vector = query_embedding.data[0].embedding

    # ----------------------------
    # Retrieve Top-K Chunks
    # ----------------------------
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=4  # top_k
    )

    retrieved_context = "\n\n".join(results["documents"][0])

    # ----------------------------
    # Add User Message
    # ----------------------------
    messages.append(
        {
            "role": "user",
            "content": f"""
Context:
{retrieved_context}

Question:
{query}
"""
        }
    )

    # ----------------------------
    # Generate Response
    # ----------------------------
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=0.2,
        top_p=1,
        max_tokens=1024,
        stream=False,
    )

    answer = completion.choices[0].message.content

    print(f"\nAssistant: {answer}")

    # Save assistant response so the model remembers the conversation
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )