#method for add node 
def add_node(v):
    if v in graph:
        print(v,"is already present in the graph")
    else:
        graph[v] = []
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
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
add_edge("A","C")
add_edge("B","D")
add_edge("B","E")
add_edge("C","D"), add_edge("D","E")
print(graph)


#DFS iteraive
def DFS_iterative(node, graph):
    visited = set()
    if node not in graph:
        print("Node is not present in the graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current =stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

DFS_iterative("C", graph)