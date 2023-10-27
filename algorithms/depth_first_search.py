"""
    GRAY: undiscovered, ORANGE: discovered, GREEN: explored
"""

# PSEUDO - CODE

"""
def DFS(graph):
    # Initalize, mark each vertex except source as undiscovered
    for each vertex u in graph except source:
        u.color = 'GRAY'

    for each vertex u in graph except source:
        if  u.color == 'GRAY':
                DFS_visit(u)


def DFS_visit(graph, u):
    u.color = 'ORANGE'

    for each vertex v in the adjancency list of u:
        if v.color == 'GRAY':
            DFS_visit(graph, v)
    
    u.color = 'GREEN' # Change the color of u to green; it is finished
"""


def DFS(graph):
    visited = set()

    def DFS_visit(node):
        visited.add(node)

        for child_node in graph[node]:
            if child_node not in visited:
                DFS_visit(child_node)

    for node in graph:
        if node not in visited:
            DFS_visit(node)

    print(visited)


adjacency_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'E': ['F'],
    'D': ['C'],
    'C': ['B'],
    'F': [],
}

DFS(adjacency_list)
