# Function to add new node to the graph with adjacent list representation

def add_node(node):
    if node in graph:
        print(node,' is already in graph')
    else:
        # create new key in graph dictionary
        graph[node] = []

# Unweighted / Undirected graph function
def add_edge_unweighted(edge1, edge2):
    if edge1 not in graph:
        print(edge1, 'is not present in graph')
    elif edge2 not in graph:
        print(edge2, 'is not present in graph')
    else:
        graph[edge1].append(edge2)
        graph[edge2].append(edge1)

def delete_node(node):
    if node not in graph:
        print(node, 'is not present in graph')
    else:
        # delete the key value pair for that node
        graph.pop(node)
        # check for node in other node's value as well
        for i in graph:
            list1 = graph[i]
            if node in list1:
                # As list1 is a list we can use remove method
                list1.remove(node) 

# Weighted / Directed graph function
def add_edge_weighted(edge1, edge2, cost):
    if edge1 not in graph:
        print(edge1, 'is not present in graph')
    elif edge2 not in graph:
        print(edge2, 'is not present in graph')
    else:
        list1 = [edge2, cost]
        list2 = [edge1, cost]
        graph[edge1].append(list1)
        graph[edge2].append(list2)

def delete_node_weighted(node, cost):
    if node not in graph:
        print(node, 'is not present in graph')
    else:
        # delete the key value pair for that node
        graph.pop(node)
        # check for node in other node's value as well
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if node == j[0]:
                    list1.remove(j)
                    break


#############################   TRAVERSAL GRAPH - DFS(RECURSIVE)    #############################

def DFS_recursive(node, visited, graph):
    if node not in graph:
        print(node, ' is not present in graph')
        return
    # Check node is visited or not
    if node not in visited:
        print(node)
        # if node is not in visited than add it to visited as we have visited it
        visited.add(node)
        for i in graph[node]:
            # Unweighted 
            DFS_recursive(i, visited, graph)
            # weighted 
            # DFS_recursive(i[0], visited, graph)


#############################   TRAVERSAL GRAPH - DFS(ITERATIVE)    #############################
def DFS_iterative(node, graph, visited):
    if node not in graph:
        print(node, ' is not present in graph')
        return
    stack = []
    stack.append(node)
    while stack:
        poppedEle = stack.pop()
        if poppedEle not in visited:
            print(poppedEle)
            visited.add(poppedEle)
            for i in graph[poppedEle]:
                stack.append(i)
                # Weghted 
                # stack.append(i[0])

    # Check node is visited or not

visited = set()
# Create dictionary
graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge_unweighted('A', 'B')
add_edge_unweighted('A', 'C')
add_edge_unweighted('B', 'E')
add_edge_unweighted('A', 'D')
add_edge_unweighted('B', 'D')
# add_edge_weighted('A', 'B', 10)
# add_edge_weighted('B', 'E', 30)
# add_edge_weighted('A', 'D', 4)
# add_edge_weighted('B', 'D', 5)
# add_edge_weighted('C', 'D', 2)
# add_edge_weighted('E', 'D', 7)
# print(graph)
# starting_node = input('Enter the starting node')
# DFS_recursive('A', visited, graph)
DFS_iterative('A', graph, visited)
# delete_node('C')
# delete_node_weighted('C', 10)
# print(graph)