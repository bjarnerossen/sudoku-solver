import random
import copy
import terminaltables
from termcolor import colored

def main():
    # Define the menu options
    options = [
        ["Difficulty", "Description"],
        ["1", "Easy"],
        ["2", "Medium"],
        ["3", "Intermediate"],
        ["4", "Extreme"]
    ]   

    # Create the table
    table = terminaltables.AsciiTable(options)

    # Print the table
    print(table.table)

    # Get user input for difficulty level
    while True:
        try:
            difficulty = int(input("Choose difficulty (1-4): "))
            if difficulty < 1 or difficulty > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Generate Sudoku board and its copy
    puzzle = generate_sudoku_board(difficulty)
    puzzle_copy = copy.deepcopy(puzzle)
    
    # Solve Sudoku board
    solution = solve_sudoku(puzzle)
    
    # Print the puzzle and its solution
    print(colored("PUZZLE:", attrs=["bold"]))
    print_puzzle(puzzle_copy)
    print()
    print(colored("SOLUTION:", attrs=["bold"]))
    print_solution(puzzle_copy, solution)

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

def print_puzzle(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        for j in range(len(board[i])):
            if j % 3 == 0:
                print("| ", end="")
            if board[i][j] == 0:
                print(colored("?", "white", "on_black", attrs=["bold"]) + " ", end="")
            else:
                print(str(board[i][j]) + " ", end="")
            if j == 8:
                print("|")
    print("+-------+-------+-------+")

def print_solution(puzzle, solved):
    for i in range(len(solved)):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        for j in range(len(solved[i])):
            if j % 3 == 0:
                print("| ", end="")
            if puzzle[i][j] == 0:
                print(colored(str(solved[i][j]) + " ", "light_green", attrs=["bold"]), end="")
            else:
                print(str(solved[i][j]) + " ", end="")
            if j == 8:
                print("|")
    print("+-------+-------+-------+")

if __name__ == "__main__":
    main()