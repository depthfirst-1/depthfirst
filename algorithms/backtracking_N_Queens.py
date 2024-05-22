def print_final_board(board, N):
    final_board = [['-'] * N for _ in range(N)]
    for col, row in enumerate(board):
        final_board[row][col] = 'Q'
        
    print(final_board)
        
def solve_N_Queens(N):
    board = [0] * N
    if place_queen(board, N, 0):
        print_final_board(board, N)
    else:
        return False
        
def place_queen(board, N, column) -> bool:
    if column == N:
        return True

    for row in range(N):
        # Assign the row where the queen can potentially be placed.
        board[column] = row
        if is_safe(board, column) and place_queen(board, N, column + 1):
            return True
        # backtrack
        board[column] = '-'
    
    return False

def is_safe(board, column):
    for i in range(column):
        # Same row
        if board[i] == board[column]:
            return False
        # Diagonal. The difference in the columns and the difference in the placement of the queens is the same
        # and so, there is a conflict. 
        if column - i == abs(board[column] - board[i]):
            return False
    return True


solve_N_Queens(8)
