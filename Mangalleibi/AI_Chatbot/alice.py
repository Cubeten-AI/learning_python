from openai import OpenAI
import chromadb
import os
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="documents"
)
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
with open("alice.txt", "r", encoding="utf-8") as f:
    document = f.read()
chunks = chunk_text(document)
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
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=4
    )
    retrieved_context = "\n\n".join(results["documents"][0])
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
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )