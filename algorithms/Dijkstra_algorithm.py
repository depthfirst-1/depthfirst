import heapq
import math


def shortest_path(graph, source, destination):
    distances = {}

    for key, _ in graph.items():
        distances[key] = math.inf

    distances[source] = 0
    explored = set()

    heap = []
    # Push the source and its distance to the min heap or priority queue.
    heapq.heappush(heap, (0, source))

    while heap:
        _, node = heapq.heappop(heap)
        if node in explored:
            continue
        explored.add(node)

        for connected_node, distance in graph[node]:
            if connected_node in explored:
                continue

            # if the current node's distance + distance to the connected node
            # is less than the distance of the connected node we have on record,
            # replace that distance and push the connected node into the priority heap.
            if distances[node] + distance < distances[connected_node]:
                distances[connected_node] = distances[node] + distance
                heapq.heappush(heap, (distances[connected_node],
                                      connected_node))

    return distances[destination]

gph = {
    'A': [('B', 5), ('F', 4), ('C', 2)],
    'B': [('E', 3), ('C', 9), ('A', 5)],
    'C': [('A', 2), ('B', 9), ('D', 5)],
    'D': [('B', 8), ('C', 5)],
    'E': [('B', 3), ('F', 6)],
    'F': [('E', 6), ('A', 4)],
}

print(shortest_path(gph, 'C', 'E'))
