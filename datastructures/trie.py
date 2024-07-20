from typing import List


class TrieNode():
    def __init__(self, char=''):
        # To store the value of a particular key
        self.char = char
        # A dictionary that contains child nodes.
        self.children = {}
        # true if the node represents the end of word
        self.is_word_end = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return

        curr_node = self.root
        # Iterate the trie with the given character index
        for char in word:
            # Add the character if it's not in the dictionary
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)
                print(char + " inserted")

            curr_node = curr_node.children[char] 

        # Mark the end character as leaf node
        curr_node.is_word_end = True
        print("'" + word + "' inserted")

    def search(self, word):
        if not word:
            return False
        curr_node = self.root
        # Iterate the trie with the given character index,
        for char in word:
            # If char not in the dictionary
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char] 

        if curr_node.is_word_end:
            return True

        return False

    def has_prefix(self, word):
        if not word:
            return False

        curr_node = self.root
        # Iterate the trie with the given character index,
        for char in word:
            # If char not in the dictionary
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True

    def dfs(self, node, prefix, result):
        if node.is_word_end:
            result.append(prefix)
            return

        for char, child_node in node.children.items():
            self.dfs(child_node, prefix + char, result)

    def suggestions(self, prefix) -> List[str]:
        curr_node = self.root
        # We go down to the final node of the prefix.
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]

        result = []
        self.dfs(curr_node, prefix, result)
        return result
