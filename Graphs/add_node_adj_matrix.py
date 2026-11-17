
def add_node(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)

        #Add zero to an existing row
        for n in graph:
            n.append(0)
            
        #Add a new row of zeros
        temp =[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end = " ")
        print()



nodes = []
graph = []
node_count = 0

print("Before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")

print("\nAfter Adding")
print("nodes:", nodes)
print(graph)
print_graph()



