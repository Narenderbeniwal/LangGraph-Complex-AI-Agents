from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
import os

load_dotenv()

# Define state
class AgentState(TypedDict):
    message: List[HumanMessage]

# LLM
llm = ChatOpenAI(model="gpt-4o")

# Node function
def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["message"])
    print(f"\nAI: {response.content}")
    return {"message": [HumanMessage(content=response.content)]}

# Build graph
graph = StateGraph(AgentState)
graph.add_node("process", process)

# Connect nodes
graph.add_edge(START, "process")
graph.add_edge("process", END)

# Compile graph
app = graph.compile()

# Run
user_input = input("Enter: ")
while user_input != "exit":
  app.invoke({"message": [HumanMessage(content=user_input)]})
  user_input = input("Enter: ")

