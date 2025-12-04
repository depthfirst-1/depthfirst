from collections import defaultdict
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Build adjacency list
    graph = defaultdict(list)
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)

    # GRAY: Undiscovered, ORANGE: Discovered, GREEN: Explored
    color = {i: 'GRAY' for i in range(numCourses)}

    def dfs(node):
        if color[node] == 'ORANGE':
            return True  # cycle detected

        if color[node] == 'GREEN':
            return False  # already explored

        color[node] = 'ORANGE'  # mark as discovered

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        color[node] = 'GREEN'  # mark as explored
        return False

    for node in range(numCourses):
        if color[node] == 'GRAY':
            if dfs(node):  # RUN DFS only if the state is undiscovered.
                return False  # cycle found

    return True  # no cycles detected
