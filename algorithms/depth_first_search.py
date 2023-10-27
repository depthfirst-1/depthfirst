explored = set()

def DFS(graph):

    for node in graph:
        if node not in explored:
            DFS_visit(node, graph)

    print(explored)

def DFS_visit(node, graph):
        explored.add(node)

        for child_node in graph[node]:
            if child_node not in explored:
                DFS_visit(child_node, graph)


adjacency_list = {
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'D': ['C'],
    'C': ['B'],
    'E': [],
    'F': ['E'], 
    'G': ['H'],
    'H': []
} 


DFS(adjacency_list)
