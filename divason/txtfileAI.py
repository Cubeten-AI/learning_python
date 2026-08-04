from openai import OpenAI
import chromadb
from dotenv import load_dotenv
import os

# ============================================================
# LOAD .ENV
# ============================================================

load_dotenv()

api_key = os.getenv("api_key")

if not api_key:
    raise ValueError(
        "API key not found. Please check your .env file."
    )


# ============================================================
# NVIDIA CLIENT
# ============================================================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)


# ============================================================
# CHROMADB
# ============================================================

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="documents"
)


# ============================================================
# MODELS
# ============================================================

EMBEDDING_MODEL = "nvidia/nv-embed-v1"

CHAT_MODEL = "openai/gpt-oss-120b"


# ============================================================
# TEXT CHUNKING
# ============================================================

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


# ============================================================
# READ TXT FILE
# ============================================================

try:

    with open(
        "keibukeuoiba.txt",
        "r",
        encoding="utf-8"
    ) as f:

        document = f.read()

except FileNotFoundError:

    print(
        "Error: keibukeuoiba.txt was not found."
    )

    exit()


# ============================================================
# CREATE CHUNKS
# ============================================================

chunks = chunk_text(document)

print(
    f"Created {len(chunks)} chunks."
)


# ============================================================
# GENERATE DOCUMENT EMBEDDINGS
# ============================================================

embeddings = []

print("Creating embeddings...")


for i, chunk in enumerate(chunks):

    response = client.embeddings.create(

        input=[chunk],

        model=EMBEDDING_MODEL,

        encoding_format="float",

        extra_body={
            "input_type": "passage",
            "truncate": "NONE"
        }
    )

    embeddings.append(
        response.data[0].embedding
    )

    print(
        f"Embedding {i + 1}/{len(chunks)}"
    )


# ============================================================
# STORE DOCUMENTS
# ============================================================

ids = [
    f"chunk_{i}"
    for i in range(len(chunks))
]

collection.upsert(

    ids=ids,

    documents=chunks,

    embeddings=embeddings
)

print(
    f"\nStored {len(chunks)} chunks in ChromaDB."
)


# ============================================================
# CHAT MEMORY
# ============================================================

messages = [

    {
        "role": "system",

        "content": (
            "You are a helpful assistant. "
            "Use the retrieved context to answer "
            "the user's question. "
            "If the answer is not in the context, "
            "say you don't know. "
            "Do not make up information."
        )
    }

]


# ============================================================
# CHAT LOOP
# ============================================================

while True:

    query = input("\nYou: ")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if query.lower().strip() in [
        "exit",
        "quit",
        "bye"
    ]:

        print(
            "Assistant: Goodbye!"
        )

        break


    # ========================================================
    # EMBED USER QUESTION
    # ========================================================

    query_embedding = client.embeddings.create(

        input=[query],

        model=EMBEDDING_MODEL,

        encoding_format="float",

        extra_body={
            "input_type": "query",
            "truncate": "NONE"
        }
    )

    query_vector = (
        query_embedding.data[0].embedding
    )


    # ========================================================
    # SEARCH CHROMADB
    # ========================================================

    results = collection.query(

        query_embeddings=[
            query_vector
        ],

        n_results=4
    )


    # ========================================================
    # RETRIEVED CONTEXT
    # ========================================================

    retrieved_context = "\n\n".join(
        results["documents"][0]
    )


    # ========================================================
    # USER MESSAGE
    # ========================================================

    messages.append(

        {
            "role": "user",

            "content": f"""
Use the following context to answer the question.

Context:
{retrieved_context}

Question:
{query}
"""
        }

    )


    # ========================================================
    # GENERATE ANSWER
    # ========================================================

    completion = client.chat.completions.create(

        model=CHAT_MODEL,

        messages=messages,

        temperature=0.2,

        top_p=1,

        max_tokens=1024,

        stream=False
    )


    # ========================================================
    # GET ANSWER
    # ========================================================

    answer = (
        completion
        .choices[0]
        .message
        .content
    )


    print(
        f"\nAssistant: {answer}"
    )


    # ========================================================
    # SAVE ANSWER TO MEMORY
    # ========================================================

    messages.append(

        {
            "role": "assistant",

            "content": answer
        }

    )