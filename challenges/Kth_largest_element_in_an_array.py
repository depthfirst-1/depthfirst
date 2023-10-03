import heapq


def findKthLargest_1(nums, k) -> int:
    heap = []

    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def partition(p, r, nums):
    pivot = nums[r]
    i = p - 1

    for j in range(p, r):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[r] = nums[r], nums[i]

    return i


def findKthLargest_2(nums, k) -> int:
    smallest_index = len(nums) - k

    def smallest(p, r):
        if p == r:
            return nums[p]

        q = partition(p, r, nums)
        if q == smallest_index:
            return nums[q]

        if q > smallest_index:
            return smallest(p, q - 1)  # search the lower half
        else:
            return smallest(q + 1, r)  # search the upper half

    return smallest(0, len(nums) - 1)
