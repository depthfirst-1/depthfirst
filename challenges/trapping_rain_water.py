def trap(height) -> int:
    N = len(height)

    left_max = []
    max_height = 0
    for i in range(N):
        left_max.append(max_height)
        max_height = max(max_height, height[i])

    right_max = []
    max_height = 0
    for j in range(N - 1, -1, -1):
        right_max.insert(0, max_height)
        max_height = max(max_height, height[j])

    count = 0
    for i in range(len(height)):
        water_height = min(left_max[i], right_max[i]) - height[i]
        if water_height > 0:
            count += water_height

    return count
