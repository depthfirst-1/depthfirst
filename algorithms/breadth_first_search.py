from collections import deque

def breadth_first_search(graph, source):
    queue = deque()
    explored = set()
    output = []

    # Add the source node
    queue.append(source)
    explored.add(source)

    while queue:
        queue_length = len(queue)
        
        for i in range(queue_length):
            node = queue.popleft()
            output.append(node)

            for neighbor in graph[node]:
                if neighbor not in explored:
                    queue.append(neighbor)
                    explored.add(neighbor)

    print(output)

adjacency_list = {
    'A': ['C'],
    'B': ['D', 'A'],
    'C': [ ],
    'D': ['E', 'F'],
    'E': ['F'],
    'F': [ ],
}

breadth_first_search(adjacency_list, 'B')
