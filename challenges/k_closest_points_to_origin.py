from math import sqrt
from heapq import heapq


def k_closest(points, k):
    heap = []

    for point in points:
        x, y = point
        d = sqrt(x**2 + y**2)
        heapq.heappush(heap, (-d, point))

        while len(heap) > k:
            heapq.heappop(heap)

    return [n[1] for n in heap]
