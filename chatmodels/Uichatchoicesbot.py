from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)

# Page Configuration
st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stChatMessage {
    border-radius: 10px;
    padding: 10px;
}
.title {
    text-align: center;
    color: #4A90E2;
    font-size: 40px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🤖 AI Personality Chatbot</p>',
            unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Select AI Mode")

    mode_option = st.selectbox(
        "Choose Personality",
        ["😡 Angry", "😂 Funny", "😢 Sad"]
    )

    if mode_option == "😡 Angry":
        mode = (
            "You are an angry AI agent. "
            "You respond aggressively and impatiently."
        )
    elif mode_option == "😂 Funny":
        mode = (
            "You are a funny AI agent. "
            "You respond with humor and jokes."
        )
    else:
        mode = (
            "You are a sad AI agent. "
            "You respond in a melancholy tone."
        )

# Model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9
)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Display Chat History
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# User Input
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.write(response.content)