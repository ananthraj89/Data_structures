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



def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


nodes = []
graph = []
node_count = 0
graph = {}

add_node("A")
add_node("B")
add_node("C")

add_edge("A","B",10)
print(graph)
