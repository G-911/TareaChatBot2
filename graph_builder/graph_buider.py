from langgraph.graph import START, END, MessagesState, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import AIMessage

from graph_nodes.graph_nodes import chatbot, log_input, handle_error

def route_based_on_response(state: MessagesState):
    last_message = state["messages"][-1]
    if isinstance(last_message,AIMessage) and "error" in last_message.content.lower():
        return "error"
    return "ok"

def build_graph():
    workcflow = StateGraph(MessagesState)

    workcflow.add_node("logger", log_input)
    workcflow.add_node("chatbot", chatbot)
    workcflow.add_node("error_handler", handle_error)

    workcflow.add_edge(START, "logger")
    workcflow.add_edge("logger", "chatbot")

    workcflow.add_conditional_edges("chatbot", route_based_on_response, {
        "ok": END,
        "error": "error_handler"
    })

    workcflow.add_edge("chatbot", END)

    memory = MemorySaver()
    graph = workcflow.compile(memory)
    return graph, workcflow