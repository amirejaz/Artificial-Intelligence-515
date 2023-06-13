def solveNQueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    return solutions

def backtrack(board, col, solutions):
    if col == len(board):
        # Add the solution to the list of solutions
        solutions.append([''.join(row) for row in board])
        return

    for row in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, col+1, solutions)
            board[row][col] = '.'

def is_valid(board, row, col):
    n = len(board)

    # Check if there is a queen in the same row
    for i in range(n):
        if board[row][i] == 'Q':
            return False

    # Check if there is a queen in the same column
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the same diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row+1, n, 1), range(col+1, n, 1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n, 1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row+1, n, 1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

# print the solution 
solutions = solveNQueens(4)
for sol in solutions:
    print(sol)
print("There are" ,len(solutions), "distinct solutions of", len(sol) , "x", len(sol), "board.")
