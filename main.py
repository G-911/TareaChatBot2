import os

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')

model = ChatMistralAI(api_key = MISTRAL_API_KEY)

workcflow = StateGraph(MessagesState)

def chat_bot(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

workcflow.add_node("chatbot", chat_bot)

workcflow.add_edge(START, "chatbot")
workcflow.add_edge("chatbot", END)

memory = MemorySaver()
graph = workcflow.compile(memory)

graph

print("Nodos:", workcflow.nodes)
print("Transiciones:", workcflow.edges)

# def describe_graph(graph: StateGraph):
#     print("📍 Estructura del Grafo:")
#     for source, targets in graph.edges.items():
#         for target in targets:
#             print(f"{source} --> {target}")

# describe_graph(workcflow)

from langchain_core.messages import HumanMessage, AIMessage

config = {"configurable": {"thread_id": "abc123"}}

query = "como me llamo?"

input_messages = HumanMessage(content = query)
output = graph.invoke({"messages": input_messages}, config)

for m in output["messages"]:
    m.pretty_print()