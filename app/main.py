import copy
import terminaltables
from termcolor import colored
import sys
from helpers import *

def main():
    # Define the difficulty levels as a dictionary
    DIFFICULTY_LEVELS = {
        1: "Easy",
        2: "Medium",
        3: "Intermediate",
        4: "Extreme"
    }

    # Define the menu options
    options = [
        ["Difficulty", "Description"],
        *[[str(k), v] for k, v in DIFFICULTY_LEVELS.items()]
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
        except KeyboardInterrupt:
            sys.exit()

    # Generate Sudoku board and its copy
    puzzle = generate_sudoku_board(difficulty)
    puzzle_copy = copy.deepcopy(puzzle)
    
    # Solve Sudoku board
    solution = solve_sudoku(puzzle)
    
    print(colored("\nPUZZLE:", attrs=["bold"]))
    print_puzzle(puzzle_copy)
    while True:
        try:
            user_input = str(input())
            if not validate_user_input(user_input):
                raise ValueError
            if user_input.lower() in ["help", "h"]:
                print(colored(
"""
Sudoku is a logic-based number placement puzzle. 
The goal is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 sub-grids contains all of the digits from 1 to 9. 
Each digit can only appear once in each row, column, and sub-grid. 
Good luck!
"""
                , attrs=["blink"]))
            elif user_input.lower() in ["solve", "s"]:
                    # Print the puzzle and its solution
                    print()
                    print(colored("SOLUTION:", attrs=["bold"]))
                    print_solution(puzzle_copy, solution)
                    break
        except ValueError:
                print('Command not found. Options: "help", "solve", "h", "s"')
            
        except KeyboardInterrupt:
            sys.exit()

def validate_user_input(user_input):
    """
    Validates user input for "help" and "solve" commands.
    Returns True if the input is valid, False otherwise.
    """
    valid_commands = ["help", "solve", "h", "s"]
    return user_input.lower() in valid_commands

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