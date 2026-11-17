def add_node(v):
    if v in graph:
        print(v,"is already present in the graph")
    else:
        graph[v] = []
graph = {}
add_node("A")
add_node("B")
add_node("C")
print(graph)

#To add edge
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not in the graph")
    elif v2 not in graph:
        print(v2,"is not in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

add_edge("A","B")
print(graph)