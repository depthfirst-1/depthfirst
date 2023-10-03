def lengthOfLongestSubstring(s):
    max_length = 0
    i = 0 
    hash_map = {}

    for j in range(len(s)):
        char = s[j]
        # character is repeated as it exists in the dict
        if char in hash_map:
            if hash_map[char] + 1 > i:
                i = hash_map[char] + 1

        # update the index of the character in the dict
        hash_map[char] = j
        substr_len = j - i + 1
        max_length = max(max_length, substr_len)

    return max_length
