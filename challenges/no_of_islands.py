def get_neighbours(row, col, ROWS, COLS):
    moves = [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1)
    ]
    valid_moves = []
    for r, c in moves:
        if 0 <= r < ROWS and 0 <= c < COLS:
            valid_moves.append((r, c))

    return valid_moves       


def numIslands(grid) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()

    def dfs(row, col):
        visited.add((row, col))
        for neigh_r, neigh_c in get_neighbours(row, col, ROWS, COLS):
            # if the cell is a land and has not been visited, then we run dfs
            # on it.
            if grid[neigh_r][neigh_c] == '1' and (neigh_r, neigh_c) not in visited:
                dfs(neigh_r, neigh_c)

    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '1' and (row, col) not in visited:
                dfs(row, col)
                count += 1

    return count
