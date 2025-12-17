from collections import deque, defaultdict


def ladder_length(begin_word, end_word, word_list):
    """
    Finds the length of the shortest transformation sequence from
    begin_word to end_word.
    """
    # If the end_word is not in the word_list, a transformation is impossible
    if end_word not in word_list:
        return 0

    # Create a defaultdict to store patterns and their corresponding words
    adj_list = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            # Create a pattern by replacing one character with a wildcard '*'
            word_ls = list(word)
            word_ls[i] = '*'
            pattern = ''.join(word_ls)
            adj_list[pattern].append(word)

    # Initialize a queue for BFS, storing (word, steps)
    queue = deque()
    queue.append((begin_word, 1))

    # Keep track of visited words to avoid cycles
    visited = {begin_word}

    # Perform Breadth-First Search
    while queue:
        word, steps = queue.popleft()

        # If the current word is the end_word, return the number of steps
        if word == end_word:
            return steps

        # Generate all possible patterns for the current word
        for i in range(len(word)):
            word_ls = list(word)
            word_ls[i] = '*'
            pattern = ''.join(word_ls)

            # Get all words that match the current pattern
            children = adj_list[pattern]
            for child in children:
                if child not in visited:
                    queue.append((child, steps + 1))
                    visited.add(child)

    return 0
