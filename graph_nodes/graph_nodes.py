from langgraph.graph import MessagesState
from model.model import model

def chatbot(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}