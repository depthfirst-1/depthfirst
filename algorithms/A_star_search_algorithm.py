import math
import heapq

def get_manhattan_distance(node_coord, destination_coord):
    dist = abs(destination_coord[0] - node_coord[0]) + abs(destination_coord[1] - node_coord[1])
    return dist
    

def A_start_search(graph, coordinates, source, destination):
    g_score = {}
    
    for key, _ in graph.items():
        g_score[key] = math.inf
        
    g_score[source] = 0
    explored = set()
    heap = []
    # Push the source and its distance to the min heap or priority queue.
    heapq.heappush(heap, (0, source))
        
    while heap:
        _, node = heapq.heappop(heap)
        if node == destination:
            return g_score[node]
        
        if node in explored:
            continue
        explored.add(node)
        
        for connected_node, cost in graph[node]:
            if connected_node in explored:
                continue
            
            # cost from the source node to current connected node
            g_cost = g_score[node] + cost 
            # heuristic cost. Manhattan cost from current connected node to destination
            h_cost = get_manhattan_distance(coordinates[connected_node], coordinates[destination])
            f_cost = g_cost + h_cost
            
            if g_cost < g_score[connected_node]:
                g_score[connected_node] = g_cost
                heapq.heappush(heap, (f_cost, connected_node)) 
    
    return None

gph = {
    'A': [('B', 1), ('C', 2), ('E', 4), ('F', 5)],
    'B': [('A', 1), ('C', 1)],
    'C': [('A', 2), ('B', 1), ('D', 3)],
    'D': [('C', 3)],
    'E': [('A', 4), ('I', 4)],
    'F': [('A', 5), ('G', 10), ('H', 11)],
    'G': [('I', 5), ('F', 10)],
    'H': [('F', 11), ('I', 5)],
    'I': [('E', 4), ('G', 5), ('H', 5)]
}

coordintates = {
    'A': (3, 3),
    'B': (2, 2),
    'C': (3, 2),
    'D': (3, 1),
    'E': (4, 5),
    'F': (5, 4),
    'G': (7, 4),
    'H': (8, 3),
    'I': (9, 6)
}

print(A_start_search(gph, coordintates, 'A', 'I'))
