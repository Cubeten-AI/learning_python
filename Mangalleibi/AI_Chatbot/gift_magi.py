from openai import OpenAI
from pypdf import PdfReader
import chromadb
import os

# -----------------------------
# NVIDIA API
# -----------------------------
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

# -----------------------------
# ChromaDB
# -----------------------------
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("gift_magi")


# -----------------------------
# Split text into chunks
# -----------------------------
def chunk_text(text):

    chunks = []

    size = 500
    overlap = 50

    start = 0

    while start < len(text):

        end = start + size

        chunks.append(text[start:end])

        if end >= len(text):
            break

        start = start + size - overlap

    return chunks


# ----------------------------------------------------
# Only create embeddings if database is empty
# ----------------------------------------------------
if collection.count() == 0:

    print("Reading PDF...")

    reader = PdfReader("Gift_Magi.pdf")

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    print("PDF Loaded.")
    print("Characters:", len(text))

    chunks = chunk_text(text)

    print("Total Chunks:", len(chunks))

    ids = []
    embeddings = []

    for i, chunk in enumerate(chunks):

        print(f"Embedding {i+1}/{len(chunks)}")

        try:

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

            ids.append(f"chunk_{i}")

        except Exception as e:

            print("Embedding Error:")
            print(e)
            exit()

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print("\nDatabase Created Successfully!\n")

else:

    print("Database already exists.")
    print("Skipping embedding creation.\n")


# ----------------------------------------------------
# Chat
# ----------------------------------------------------

messages = [

    {
        "role": "system",
        "content":
        "You are a cheerful AI storyteller. "
        "Answer only from the provided context. "
        "If the answer is not found, politely say "
        "'I couldn't find that in the story.'"
    }

]

print("===================================")
print(" Gift of Magi AI Chatbot")
print("===================================")
print("Type 'exit' to quit.\n")


while True:

    question = input("You : ")

    if question.lower() in ["exit", "quit", "bye"]:

        print("\nAssistant: Goodbye!")
        break

    try:

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

    except Exception as e:

        print("Query Embedding Error")
        print(e)
        continue

    results = collection.query(

        query_embeddings=[query_vector],

        n_results=4

    )

    context = "\n".join(results["documents"][0])

    messages.append(

        {
            "role": "user",
            "content": f"""

Context:

{context}

Question:

{question}

"""
        }

    )

    print("\nThinking...\n")

    try:

        completion = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=messages,

            temperature=0.2,

            max_tokens=300,

            stream=False

        )

        answer = completion.choices[0].message.content

        print("Assistant:", answer)

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:

        print("Chat Error")
        print(e)