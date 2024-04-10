# O(N) solution
def Kth_missing_positive_number_1(arr, k):
    arr_set = set(arr)

    for i in range(1, len(arr) + k+ 1):
        if i not in arr_set:
            k -= 1
        if k == 0:
            return i

# Binary Search solution O(log N)
def Kth_missing_positive_number_2(arr, k):
    low = 0
    high = len(arr) - 1
        
    while low <= high:
        mid = (low + high) // 2
        # Count of number of missing elements before mid
        missing = arr[mid] - mid - 1
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
            

    return high + k + 1
