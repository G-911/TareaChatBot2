from graph_builder.graph_buider import build_graph
from langchain_core.messages import HumanMessage

graph, workcflow = build_graph()

# Opcional: imprimir nodos y transiciones
print("Nodos:", workcflow.nodes)
print("Transiciones:", workcflow.edges)

query = "como me llamo?"
input_messages = HumanMessage(content=query)
config = {"configurable": {"thread_id": "abc123"}}

output = graph.invoke({"messages": input_messages}, config)

for m in output["messages"]:
    m.pretty_print()