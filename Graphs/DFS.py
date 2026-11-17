#Graph traversal DFS (Depth First Search) algorithm, the following program for adj list representation, using
#recursion. we can choose which ever one we want to traverse but we need to vist the node only once. 

#check node exists
#visit the starting node A, #search for the adj node of A # unvisited adj node of A(B) 
     #search for the adj node B #unvisited adj node B  and so on.... use recursion #To know whether the node is 
#visited or not? that can be either in the set, list set is more preferable in this case.

def DFS(node, visited, graph):
    if node  not in graph:
        print("Node is not present in the graph")
        return 
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)

visited = set()


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



DFS("A", visited, graph)

