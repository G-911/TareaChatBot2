from langgraph.graph import START, END, MessagesState, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from graph_nodes.graph_nodes import chatbot

def build_graph():
    workcflow = StateGraph(MessagesState)
    workcflow.add_node("chatbot", chatbot)
    workcflow.add_edge(START, "chatbot")
    workcflow.add_edge("chatbot", END)

    memory = MemorySaver()
    graph = workcflow.compile(memory)
    return graph, workcflow