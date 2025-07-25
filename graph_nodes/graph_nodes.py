from langgraph.graph import MessagesState
from model.model import model
from langchain_core.messages import AIMessage

def chatbot(state: MessagesState):
    try:
        response = model.invoke(state["messages"])
        return {"messages": response}
    except Exception as e:
        print(f"[ERROR] {e}")
        return {"messages": AIMessage(content = "hubo un error procesando tu mensaje")}
    
def log_input(state: MessagesState):
    user_messages = state["messages"]
    print(f"[LOG] Entrada del usuario: {user_messages}")
    return {"messages": user_messages}

def handle_error(state: MessagesState):
    return {"messages": [AIMessage(content="Lo siento, ocurrio un error en el sistema. Intenta nuevamente")]}
