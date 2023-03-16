import random

def generate_sudoku_board(difficulty=1):
    # create empty board only containing zeros
    board = [[0 for _ in range(9)] for _ in range(9)]

    # fill in first row randomly
    for i in range(9):
        board[0][i] = i + 1
    random.shuffle(board[0])

    # fill in the rest of board
    solve_sudoku(board)

    # define num_cells based on difficulty
    if difficulty == 1:
        num_cells = 20
    elif difficulty == 2:
        num_cells = 30
    elif difficulty == 3:
        num_cells = 40
    elif difficulty == 4:
        num_cells = 60

    # randomly remove cells based on given difficulty
    remove_cells(board, num_cells)

    return board

def solve_sudoku(board):
    # find the first empty cell
    row, col = find_empty_cell(board)

    # if no empty cell is found, the sudoku is solved
    if row == -1:
        return board
    
    # try each possible number in the cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return board

    # if we tried all numbers and none worked, backtrack
    board[row][col] = 0

def find_empty_cell(board):
    # find empty cell in board and return index for row and col
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return -1, -1

def is_valid_move(board, row, col, num):
    # check row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # check subgrid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
    
    # if all checks pass, the move is valid
    return True

def remove_cells(board, num_cells):
    # remove cells randomly from board based on difficulty level
    for _ in range(num_cells):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

if __name__ == "__main__":
    pass