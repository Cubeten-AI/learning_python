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
        "Create a .env file and add:\n\n"
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
# MODELS
# ============================================================

CHAT_MODEL = "meta/muse-glimmer-30b"

EMBEDDING_MODEL = "nvidia/nv-embedqa-e5-v5"


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
# STREAMLIT CONFIG
# ============================================================

st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖",
    layout="wide",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main application */

    .stApp {
        background-color: #0e1117;
    }


    /* Sidebar */

    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }


    /* Header */

    .main-title {
        font-size: 38px;
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
        padding: 18px;
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


    /* General mode */

    .general-mode {
        background-color: #1f2937;
        color: #60a5fa;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        margin-bottom: 15px;
    }


    /* PDF mode */

    .pdf-mode {
        background-color: #0d4429;
        color: #3fb950;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        margin-bottom: 15px;
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

def chunk_text(
    text,
    chunk_size=500,
    overlap=50,
):

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

    for page in reader.pages:

        text = page.extract_text()

        if text:
            document += text + "\n"

    return document


# ============================================================
# CREATE DOCUMENT EMBEDDINGS
# ============================================================

def generate_document_embeddings(
    chunks,
    batch_size=32,
):

    all_embeddings = []

    total = len(chunks)

    progress_bar = st.progress(
        0,
        text="Generating document embeddings..."
    )

    for start in range(
        0,
        total,
        batch_size,
    ):

        batch = chunks[
            start:start + batch_size
        ]

        response = client.embeddings.create(
            input=batch,
            model=EMBEDDING_MODEL,
            encoding_format="float",
            extra_body={
                "input_type": "passage",
                "truncate": "NONE",
            },
        )

        batch_embeddings = [
            item.embedding
            for item in response.data
        ]

        all_embeddings.extend(
            batch_embeddings
        )

        progress = min(
            (start + len(batch)) / total,
            1.0,
        )

        progress_bar.progress(
            progress,
            text=(
                f"Embedding "
                f"{min(start + len(batch), total)} "
                f"of {total} chunks"
            ),
        )

    progress_bar.empty()

    return all_embeddings


# ============================================================
# QUERY EMBEDDING
# ============================================================

def generate_query_embedding(query):

    response = client.embeddings.create(
        input=[query],
        model=EMBEDDING_MODEL,
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

    document = extract_pdf_text(
        pdf_file
    )

    if not document.strip():

        raise ValueError(
            "No readable text was found in the PDF."
        )

    chunks = chunk_text(
        document
    )

    if not chunks:

        raise ValueError(
            "Could not create text chunks."
        )

    document_hash = hashlib.md5(
        pdf_file.getvalue()
    ).hexdigest()

    # --------------------------------------------------------
    # Check whether this PDF is already indexed
    # --------------------------------------------------------

    existing = collection.get(
        where={
            "document_hash": document_hash
        }
    )

    if existing["ids"]:

        return {
            "document_hash": document_hash,
            "document_name": pdf_file.name,
            "characters": len(document),
            "chunks": len(chunks),
            "already_indexed": True,
        }

    # --------------------------------------------------------
    # Generate embeddings
    # --------------------------------------------------------

    embeddings = generate_document_embeddings(
        chunks
    )

    # --------------------------------------------------------
    # IDs
    # --------------------------------------------------------

    ids = [
        f"{document_hash}_{i}"
        for i in range(len(chunks))
    ]

    # --------------------------------------------------------
    # Metadata
    # --------------------------------------------------------

    metadatas = [
        {
            "document": pdf_file.name,
            "document_hash": document_hash,
            "chunk_index": i,
        }
        for i in range(len(chunks))
    ]

    # --------------------------------------------------------
    # Store in ChromaDB
    # --------------------------------------------------------

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
        "already_indexed": False,
    }


# ============================================================
# RETRIEVE PDF CONTEXT
# ============================================================

def retrieve_context(
    query,
    document_hash,
    top_k=3,
):

    query_embedding = generate_query_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k,
        where={
            "document_hash": document_hash
        },
    )

    documents = results.get(
        "documents",
        [[]]
    )

    metadatas = results.get(
        "metadatas",
        [[]]
    )

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
        retrieved_metadata,
    ):

        sources.append(
            {
                "text": document,
                "metadata": metadata,
            }
        )

    return context, sources


# ============================================================
# GENERAL AI CHAT
# ============================================================

def general_chat_stream(
    query,
    conversation,
):

    system_message = {
        "role": "system",
        "content": (
            "You are a helpful general-purpose AI assistant. "
            "Answer questions clearly and accurately. "
            "Explain concepts when useful. "
            "If you are uncertain about something, say so. "
            "Do not claim that you know something when you do not."
            "If asked do you know the personality of me answer taking the personality of mahatma gandhi. "
            "If asked who are you just say you are 'Chaterpater, your personal ai assistant and pdf solver', don't say any other details about you ."
        ),
    }

    messages = [
        system_message
    ]

    messages.extend(
        conversation
    )

    messages.append(
        {
            "role": "user",
            "content": query,
        }
    )

    stream = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=0.3,
        top_p=0.95,
        max_tokens=7000,
        stream=True,
    )

    for chunk in stream:

        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta

        if delta.content:

            yield delta.content


# ============================================================
# PDF AI CHAT
# ============================================================

def pdf_chat_stream(
    query,
    context,
    conversation,
):

    system_message = {
        "role": "system",
        "content": (
            "You are a helpful PDF document assistant. "
            "Answer the user's question using the retrieved "
            "context from the uploaded document. "
            "Do not invent information that is not supported "
            "by the retrieved context. "
            "If the answer cannot be found in the retrieved "
            "context, clearly say that you could not find "
            "the answer in the document. "
            "Keep answers clear and useful."
        ),
    }

    messages = [
        system_message
    ]

    messages.extend(
        conversation
    )

    messages.append(
        {
            "role": "user",
            "content": f"""
Retrieved context from the PDF:

{context}

User question:

{query}
""",
        }
    )

    stream = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=0.2,
        top_p=0.95,
        max_tokens=7000,
        stream=True,
    )

    for chunk in stream:

        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta

        if delta.content:

            yield delta.content


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# 🤖 My AI Assistant"
    )

    st.caption(
        "General AI + PDF Solver"
    )

    st.divider()

    # --------------------------------------------------------
    # PDF
    # --------------------------------------------------------

    st.subheader(
        "📚 PDF Knowledge"
    )

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"],
        help=(
            "Upload a PDF if you want to ask "
            "questions about its contents."
        ),
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

                    if result[
                        "already_indexed"
                    ]:

                        st.write(
                            "⚡ PDF was already indexed."
                        )

                    else:

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
                    "PDF ready!"
                )

            except Exception as e:

                st.error(
                    f"Processing failed:\n\n{e}"
                )

    # --------------------------------------------------------
    # ACTIVE DOCUMENT
    # --------------------------------------------------------

    if st.session_state.indexed:

        st.markdown(
            """
            <div class="pdf-mode">
                📄 PDF mode enabled
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption(
            st.session_state.document_name
        )

    else:

        st.markdown(
            """
            <div class="general-mode">
                🌐 General AI mode
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # --------------------------------------------------------
    # DATABASE
    # --------------------------------------------------------

    st.subheader(
        "📊 Database"
    )

    st.metric(
        "Stored chunks",
        collection.count(),
    )

    st.divider()

    # --------------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------------

    if st.button(
        "🧹 Clear Chat",
        use_container_width=True,
    ):

        st.session_state.messages = []

        st.rerun()

    # --------------------------------------------------------
    # CLEAR DATABASE
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear PDF Database",
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

            st.session_state.document_name = None

            st.session_state.document_hash = None

            st.session_state.indexed = False

            st.session_state.messages = []

            st.success(
                "PDF database cleared."
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
    """
    <div class="main-title">
        🤖 My AI Assistant
    </div>

    <div class="subtitle">
        Ask anything, or upload a PDF and chat with it.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MODE STATUS
# ============================================================

if st.session_state.indexed:

    st.markdown(
        f"""
        <div class="document-card">

        <strong>📄 Active PDF</strong><br>

        {st.session_state.document_name}

        <br><br>

        <span style="color:#3fb950;">
        ✓ Questions will use your PDF as context
        </span>

        </div>
        """,
        unsafe_allow_html=True,
    )

else:

    st.markdown(
        """
        <div class="document-card">

        <strong>🌐 General AI Mode</strong><br>

        Ask me anything about programming,
        science, history, mathematics, technology,
        or other general topics.

        <br><br>

        <span style="color:#60a5fa;">
        Upload a PDF whenever you want document-based answers.
        </span>

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
    "Ask anything..."
)


if query:

    # --------------------------------------------------------
    # DISPLAY USER MESSAGE
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(
            query
        )

    # --------------------------------------------------------
    # ASSISTANT
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        try:

            # =================================================
            # PDF MODE
            # =================================================

            if (
                st.session_state.indexed
                and st.session_state.document_hash
            ):

                with st.spinner(
                    "🔎 Searching your PDF..."
                ):

                    context, sources = retrieve_context(
                        query=query,
                        document_hash=(
                            st.session_state.document_hash
                        ),
                        top_k=3,
                    )

                if context:

                    answer = st.write_stream(
                        pdf_chat_stream(
                            query=query,
                            context=context,
                            conversation=(
                                st.session_state.messages
                            ),
                        )
                    )

                    # --------------------------------------------
                    # SOURCES
                    # --------------------------------------------

                    with st.expander(
                        "🔎 View PDF sources"
                    ):

                        for i, source in enumerate(
                            sources
                        ):

                            metadata = source[
                                "metadata"
                            ]

                            chunk_index = metadata.get(
                                "chunk_index",
                                i,
                            )

                            st.markdown(
                                f"**Source {i + 1} — "
                                f"Chunk {chunk_index}**"
                            )

                            st.caption(
                                metadata.get(
                                    "document",
                                    "Unknown document",
                                )
                            )

                            st.write(
                                source["text"]
                            )

                            if (
                                i
                                < len(sources) - 1
                            ):

                                st.divider()

                else:

                    # --------------------------------------------
                    # If PDF has no useful result
                    # --------------------------------------------

                    answer = st.write_stream(
                        general_chat_stream(
                            query=query,
                            conversation=(
                                st.session_state.messages
                            ),
                        )
                    )

            # =================================================
            # GENERAL AI MODE
            # =================================================

            else:

                answer = st.write_stream(
                    general_chat_stream(
                        query=query,
                        conversation=(
                            st.session_state.messages
                        ),
                    )
                )

        except Exception as e:

            answer = (
                "Sorry, something went wrong.\n\n"
                f"{e}"
            )

            st.error(
                answer
            )

    # --------------------------------------------------------
    # SAVE CONVERSATION
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