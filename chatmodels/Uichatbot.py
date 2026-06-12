from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

# Initialize Model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9
)

# Page Title
st.set_page_config(
    page_title="Technical Chatbot",
    page_icon="🤖"
)

st.title("🤖 Technical Chatbot")
st.write("Ask any technical question.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are giving technical related answers")
    ]

# Display previous chat
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# User Input
if prompt := st.chat_input("Type your question here..."):

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Save user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Get response
    response = model.invoke(st.session_state.messages)

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response.content)

    # Save response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )