# Modified 7-13-2025 to use LangGraph Workflow with error handling
import os
from dotenv import load_dotenv
import streamlit as st
from workflow import build_newsgenie_workflow

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if not os.path.exists(env_path):
    st.warning(".env file not found. Make sure it exists at the project root.")
else:
    load_dotenv(dotenv_path=env_path)

st.set_page_config(page_title="NewsGenie", layout="centered")
st.title("🧞‍♂️ NewsGenie - Your AI News Assistant")

# Initialize LangGraph workflow
try:
    workflow = build_newsgenie_workflow()
except Exception as e:
    st.error("Failed to build the workflow. Please check workflow configuration.")
    st.stop()

# Streamlit UI
query = st.text_input("Ask me anything or request news:")
category = st.selectbox("Select a news category", ["technology", "finance", "sports", "health"])

# Session state to hold input and selected category
if "conversation_state" not in st.session_state:
    st.session_state.conversation_state = {"input": "", "category": "technology"}

# Run workflow on button click
if st.button("Run NewsGenie"):
    if not query:
        st.warning("Please enter a question or topic.")
    else:
        st.session_state.conversation_state["input"] = query
        st.session_state.conversation_state["category"] = category

        try:
            result = workflow.invoke(st.session_state.conversation_state)
            st.write("**NewsGenie:**")
            st.write(result.get("output", "No output returned."))
        except Exception as e:
            st.error(f"Something went wrong while processing your request: {e}")
