import os
import hashlib

import streamlit as st
import chromadb
from openai import OpenAI
from pypdf import PdfReader
from dotenv import load_dotenv


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not NVIDIA_API_KEY:
    st.error(
        "NVIDIA_API_KEY not found.\n\n"
        "Create a .env file and add:\n"
        "NVIDIA_API_KEY=your_api_key"
    )
    st.stop()


# ============================================================
# NVIDIA CLIENT
# ============================================================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY,
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
# STREAMLIT PAGE
# ============================================================

st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="🤖",
    layout="wide",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #0e1117;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
    }

    /* Main title */
    .main-title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #8b949e;
        font-size: 16px;
        margin-bottom: 30px;
    }

    /* Document card */
    .document-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* Status */
    .status {
        background-color: #0d4429;
        color: #3fb950;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        margin-bottom: 15px;
    }

    /* Chat */
    .chat-container {
        max-width: 900px;
        margin: auto;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_name" not in st.session_state:
    st.session_state.document_name = None

if "document_hash" not in st.session_state:
    st.session_state.document_hash = None

if "indexed" not in st.session_state:
    st.session_state.indexed = False


# ============================================================
# TEXT CHUNKING
# ============================================================

def chunk_text(text, chunk_size=500, overlap=50):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start += chunk_size - overlap

    return chunks


# ============================================================
# PDF EXTRACTION
# ============================================================

def extract_pdf_text(pdf_file):

    reader = PdfReader(pdf_file)

    document = ""

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:
            document += text + "\n"

    return document


# ============================================================
# NVIDIA EMBEDDING
# ============================================================

def generate_embedding(text):

    response = client.embeddings.create(
        input=[text],
        model="nvidia/nv-embedcode-7b-v1",
        encoding_format="float",
        extra_body={
            "input_type": "query",
            "truncate": "NONE",
        },
    )

    return response.data[0].embedding


# ============================================================
# INDEX PDF
# ============================================================

def index_pdf(pdf_file):

    document = extract_pdf_text(pdf_file)

    if not document.strip():
        raise ValueError(
            "No readable text was found in the PDF."
        )

    chunks = chunk_text(document)

    if not chunks:
        raise ValueError(
            "Could not create text chunks."
        )

    document_hash = hashlib.md5(
        pdf_file.getvalue()
    ).hexdigest()

    embeddings = []

    progress_bar = st.progress(
        0,
        text="Generating embeddings..."
    )

    for i, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        embeddings.append(embedding)

        progress = int(
            ((i + 1) / len(chunks)) * 100
        )

        progress_bar.progress(
            progress,
            text=f"Embedding chunk {i + 1} of {len(chunks)}"
        )

    progress_bar.empty()

    ids = [
        f"{document_hash}_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        {
            "document": pdf_file.name,
            "document_hash": document_hash,
            "chunk_index": i,
        }
        for i in range(len(chunks))
    ]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    return {
        "document_hash": document_hash,
        "document_name": pdf_file.name,
        "characters": len(document),
        "chunks": len(chunks),
    }


# ============================================================
# RETRIEVE DOCUMENT CONTEXT
# ============================================================

def retrieve_context(query, document_hash=None, top_k=4):

    query_embedding = generate_embedding(query)

    where_filter = None

    if document_hash:
        where_filter = {
            "document_hash": document_hash
        }

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where=where_filter,
    )

    documents = results.get("documents", [[]])

    metadatas = results.get("metadatas", [[]])

    if not documents or not documents[0]:
        return "", []

    retrieved_documents = documents[0]

    retrieved_metadata = (
        metadatas[0]
        if metadatas
        else []
    )

    context = "\n\n".join(
        retrieved_documents
    )

    sources = []

    for document, metadata in zip(
        retrieved_documents,
        retrieved_metadata
    ):

        sources.append(
            {
                "text": document,
                "metadata": metadata,
            }
        )

    return context, sources


# ============================================================
# GENERATE ANSWER
# ============================================================

def generate_answer(
    query,
    context,
    conversation
):

    system_message = {
        "role": "system",
        "content": (
            "You are a helpful PDF document assistant. "
            "Answer the user's question using only the "
            "provided retrieved context. "
            "If the answer cannot be found in the context, "
            "say that you don't know based on the document. "
            "Do not invent facts. "
            "Keep answers clear and useful."
        ),
    }

    messages = [
        system_message
    ]

    # Add previous conversation
    messages.extend(conversation)

    # Current question
    messages.append(
        {
            "role": "user",
            "content": f"""
Retrieved context:

{context}

User question:

{query}
""",
        }
    )

    completion = client.chat.completions.create(
        model="google/diffusiongemma-26b-a4b-it",
        messages=messages,
        temperature=0.2,
        top_p=1,
        max_tokens=1024,
        stream=False,
    )

    return completion.choices[0].message.content


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# 📚 PDF RAG"
    )

    st.caption(
        "Chat with your documents"
    )

    st.divider()

    st.subheader("📄 Document")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"],
        help="Upload a PDF to create a searchable knowledge base.",
    )

    if uploaded_file:

        st.success(
            f"Selected: {uploaded_file.name}"
        )

        process_button = st.button(
            "🚀 Process PDF",
            use_container_width=True,
            type="primary",
        )

        if process_button:

            try:

                with st.status(
                    "Processing PDF...",
                    expanded=True,
                ):

                    st.write(
                        "📖 Extracting text..."
                    )

                    result = index_pdf(
                        uploaded_file
                    )

                    st.session_state.document_name = (
                        result["document_name"]
                    )

                    st.session_state.document_hash = (
                        result["document_hash"]
                    )

                    st.session_state.indexed = True

                    st.session_state.messages = []

                    st.write(
                        f"✅ Characters: "
                        f"{result['characters']:,}"
                    )

                    st.write(
                        f"✅ Chunks: "
                        f"{result['chunks']:,}"
                    )

                    st.write(
                        "✅ Stored in ChromaDB"
                    )

                st.success(
                    "PDF processed successfully!"
                )

            except Exception as e:

                st.error(
                    f"Processing failed:\n\n{e}"
                )

    st.divider()

    st.subheader("📊 Database")

    st.metric(
        "Stored chunks",
        collection.count()
    )

    if st.session_state.indexed:

        st.markdown(
            f"""
            <div class="status">
            ✓ Document ready
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption(
            st.session_state.document_name
        )

    st.divider()

    if st.button(
        "🗑️ Clear Database",
        use_container_width=True,
    ):

        try:

            chroma_client.delete_collection(
                "documents"
            )

            collection = (
                chroma_client
                .get_or_create_collection(
                    name="documents"
                )
            )

            st.session_state.messages = []

            st.session_state.document_name = None

            st.session_state.document_hash = None

            st.session_state.indexed = False

            st.success(
                "Database cleared."
            )

            st.rerun()

        except Exception as e:

            st.error(
                f"Could not clear database: {e}"
            )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">Hi I am your personal Assistant 🤖 </div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about your PDF i am here to answer your question '
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# DOCUMENT STATUS
# ============================================================

if not st.session_state.indexed:

    st.info(
        "👈 Upload a PDF from the sidebar and click "
        "**Process PDF** to begin."
    )

else:

    st.markdown(
        f"""
        <div class="document-card">
            <strong>📄 Active Document</strong><br>
            {st.session_state.document_name}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# CHAT INPUT
# ============================================================

query = st.chat_input(
    "Ask something about your document..."
)


if query:

    # Make sure document exists
    if not st.session_state.indexed:

        st.warning(
            "Please upload and process a PDF first."
        )

        st.stop()

    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(query)

    # --------------------------------------------------------
    # RETRIEVE
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        try:

            with st.spinner(
                "🔎 Searching your document..."
            ):

                context, sources = retrieve_context(
                    query=query,
                    document_hash=(
                        st.session_state.document_hash
                    ),
                    top_k=4,
                )

            if not context:

                answer = (
                    "I couldn't find relevant information "
                    "in the document."
                )

                st.markdown(answer)

            else:

                with st.spinner(
                    "🤖 Generating answer..."
                ):

                    answer = generate_answer(
                        query=query,
                        context=context,
                        conversation=(
                            st.session_state.messages
                        ),
                    )

                st.markdown(answer)

                # ------------------------------------------------
                # SOURCES
                # ------------------------------------------------

                with st.expander(
                    "🔎 View retrieved sources"
                ):

                    for i, source in enumerate(
                        sources
                    ):

                        metadata = source[
                            "metadata"
                        ]

                        chunk_index = metadata.get(
                            "chunk_index",
                            i
                        )

                        st.markdown(
                            f"**Source {i + 1} — "
                            f"Chunk {chunk_index}**"
                        )

                        st.caption(
                            metadata.get(
                                "document",
                                "Unknown document"
                            )
                        )

                        st.write(
                            source["text"]
                        )

                        if i < len(sources) - 1:
                            st.divider()

        except Exception as e:

            answer = (
                f"Sorry, something went wrong:\n\n{e}"
            )

            st.error(answer)

    # --------------------------------------------------------
    # SAVE CHAT
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query,
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )