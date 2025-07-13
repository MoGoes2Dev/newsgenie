# app/workflow.py

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
# (25.07.13 deprecated)from langchain.memory import ChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import HumanMessage, AIMessage
# Added 25.07.13
from typing import _TypedDict
from chatbot import get_completion, classify_query
from news_api import fetch_news

# Added 25.07.13 - Define state schema first. 
# Addresses error encountered due to outdate integration
class WorkflowState(_TypedDict):
    input: str
    output: str
    query_type: str
    category: str

# Define shared memory class
class ConversationState:
    def __init__(self):
        self.history = ChatMessageHistory()

    def add_user_message(self, message):
        self.history.add_user_message(message)

    def add_ai_message(self, message):
        self.history.add_ai_message(message)

# Node: classify query type
# 25.07.13 change state from "dict" to "workflowstate"
def classify(state: WorkflowState) -> WorkflowState:
    query = state["input"]
    qtype = classify_query(query)
    state["query_type"] = qtype
    return state

# Node: handle general query
def handle_general(state: WorkflowState):
    answer = get_completion(state["input"])
    state["output"] = answer
    return state

# Node: handle news
def handle_news(state: WorkflowState):
    category = state.get("category", "technology")
    news_items = fetch_news(category)
    formatted = "\n\n".join(f"- {item['title']}" for item in news_items)
    state["output"] = formatted or "No news found."
    return state

# Build the LangGraph workflow
def build_newsgenie_workflow():
    workflow = StateGraph(WorkflowState)

    # Define states
    workflow.add_node("classify", classify)
    workflow.add_node("handle_general", handle_general)
    workflow.add_node("handle_news", handle_news)

    # Routing
    # (25.07.13 commented out workflow.set_entry_point("classify")
    #workflow.add_conditional_edges(
     #   "classify",
      #  condition=lambda state: state["query_type"],
       # path_map={
        #    "general": "handle_general",
         #   "news": "handle_news"
        #}
    #)
    #25.07.13 added to address error
    workflow.set_entry_point("classify")
    workflow.add_edge("__start__", "classify")

    workflow.add_conditional_edges (
        "classify",
        lambda state: state["query_type"],
        {
            "general": "handle_general",
            "news": "handle_news"
        }
    )

    workflow.add_edge("handle_general", END)
    workflow.add_edge("handle_news", END)

    return workflow.compile()

#Added 25.07.13 to test workflow from CLI
#if __name__ =="__main__":
 #   workflow = build_newsgenie_workflow()
  #  test_state = {
   #     "input": "Tell me a fun fact about AI",
    #    "category": "technology"
    #}
#
    #result = workflow.invoke(test_state)
    #print("\n NewsGenie Repsonse:\n")
 #   print(result["output"])