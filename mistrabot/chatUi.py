from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# ---------------- MODEL ----------------
model = ChatMistralAI(model="mistral-small-2603")

# ---------------- PROMPT ----------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional information extraction assistant.

Extract:
- Main topic
- People, organizations, locations
- Dates, years, statistics
- Key facts and key takeaways

Rules:
- Do not invent information
- If missing write 'Not Mentioned'
- Give a clean structured output with summary
            """
        ),
        (
            "human",
            "Analyze this text:\n{paragraph}"
        ),
    ]
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Extractor",
    page_icon="🎧",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #121212;
    color: white;
}

/* Title */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #1DB954;
    margin-bottom: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #181818;
}

/* Textarea */
.stTextArea textarea {
    background-color: #282828 !important;
    color: white !important;
    border-radius: 12px;
    font-size: 16px;
}

/* Button */
.stButton>button {
    background-color: #1DB954;
    color: white;
    border-radius: 25px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background-color: #1ed760;
}

/* Output card */
.card {
    background-color: #181818;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    white-space: pre-line;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg",
        width=70
    )

    st.markdown("## 🎧 Smart Extractor")
    st.markdown("---")

    st.markdown("### 📌 Features")
    st.markdown("""
    - 🎯 Entity Extraction  
    - 📊 Statistics Detection  
    - 📅 Date Recognition  
    - 🧠 Key Insights  
    - 📝 Smart Summary  
    """)

    st.markdown("---")
    st.markdown("⚡ Built with LangChain + Mistral AI")

# ---------------- MAIN UI ----------------
st.markdown('<div class="title">🎵 Information Extraction Dashboard</div>', unsafe_allow_html=True)

paragraph = st.text_area(
    "Paste your content below 👇",
    height=250,
    placeholder="Enter paragraph, article, blog, or document text..."
)

# ---------------- BUTTON ACTION ----------------
if st.button("🚀 Extract Insights"):
    if paragraph.strip():

        with st.spinner("Analyzing content..."):

            final_prompt = prompt.invoke(
                {"paragraph": paragraph}
            )

            response = model.invoke(final_prompt)

            st.markdown("### 📊 Extracted Insights")

            st.markdown(
                f'<div class="card">{response.content}</div>',
                unsafe_allow_html=True
            )

    else:
        st.warning("Please enter some text first ⚠️")