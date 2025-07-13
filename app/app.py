# Modified 7-13-2025 to use LangGraph Workflow
import os
from dotenv import load_dotenv
import streamlit as st
from workflow import build_newsgenie_workflow

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

st.set_page_config(page_title="NewsGenie", layout="centered")
st.title("🧞‍♂️ NewsGenie - Your AI News Assistant")

# Initialize LangGraph workflow
workflow = build_newsgenie_workflow()

# Streamlit UI
query = st.text_input("Ask me anything or request news:")
category = st.selectbox("Select a news category", ["technology", "finance", "sports", "health"])

# Session state to hold input and selected category
if "conversation_state" not in st.session_state:
    st.session_state.conversation_state = {"input": "", "category": "technology"}

# Run workflow on button click
if st.button("Run NewsGenie"):
    st.session_state.conversation_state["input"] = query
    st.session_state.conversation_state["category"] = category

    result = workflow.invoke(st.session_state.conversation_state)
    st.write("**NewsGenie:**")
    st.write(result["output"])