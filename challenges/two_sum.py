def twoSum(nums, target):
    hashmap = {}

    for index, num in enumerate(nums):
        if target - num in hashmap:
            return index, hashmap[target - num]
        hashmap[num] = index

    return None
