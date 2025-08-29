from typing import TypedDict, List,Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    message: List[Union[HumanMessage,AIMessage]]

llm = ChatOpenAI(model="gpt-4o")

def process(state: AgentState) -> AgentState:
    """This node will solve the request you input"""
    responcse = llm.invoke(state["message"])

    state["message"].append(AIMessage(content=responcse.content))
    print(f"\nAI: {responcse.content}")
    print("Current STATE:",state["message"])
    return state

# Build graph
graph = StateGraph(AgentState)
graph.add_node("process", process)

# Connect nodes
graph.add_edge(START, "process")
graph.add_edge("process", END)

# Compile graph
agent = graph.compile()

conversation_history = []

user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"message": conversation_history})
    conversation_history = result["message"]
    user_input = input("Enter: ")

with open("logging.txt", "w") as file:
    file.write("Your Conversation Log:\n")
    
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n\n")
    file.write("End of Conversation")

print("Conversation saved to logging.txt")


    
