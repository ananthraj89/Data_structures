#for un directed weighted graph

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


def add_edge(v1,v2, cost):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")

    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost


nodes = []
graph = []
node_count = 0


print("Before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")

print("\nAfter Adding")
print("nodes:", nodes)
print(graph)
print_graph()

add_edge("A", "B", 10)
print("\nAfter Adding Edge A-B with cost 10")
print_graph()

add_edge("B", "C", 20)
print("\nAfter Adding Edge B-C with cost 20")
print_graph()

add_edge("A", "C", 30)
print("\nAfter Adding Edge A-C with cost 30")
print_graph()