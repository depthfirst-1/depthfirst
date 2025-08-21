from typing import List

class Solution:
    def get_neighbors(self, row, col, ROWS, COLS):
        directions = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]
        return [
            (r, c) for r, c in directions
            if 0 <= r < ROWS and 0 <= c < COLS
        ]
   
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set() 
        
        def dfs(row, col, index):
            if board[row][col] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True 

            visited.add((row, col))
            print(visited)
            
            for neigh_r, neigh_c in self.get_neighbors(row, col, ROWS, COLS):
                if (neigh_r, neigh_c) not in visited:
                    if dfs(neigh_r, neigh_c, index + 1):
                        return True

            visited.remove((row, col))
            return False

        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
                        
        return False
