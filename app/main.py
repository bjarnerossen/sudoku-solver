from copy import deepcopy # Used to create a deep copy of the Sudoku board
import terminaltables # Used to print the user menu in a tabular format
from termcolor import colored # Used to colorize output text
import sys # Used to handle keyboard interrupt and exit the program

import helpers # Contains helper functions to generate and solve Sudoku puzzles

# Define the difficulty levels as a dictionary
DIFFICULTY_LEVELS = {
    1: "Easy",
    2: "Medium",
    3: "Intermediate",
    4: "Extreme"
}

def main():
    # Print the user menu
    print_user_menu()

    # Get user input for difficulty level
    difficulty = get_user_difficulty()

    # Generate Sudoku board and its copy
    puzzle = helpers.generate_sudoku_board(difficulty)
    puzzle_copy = deepcopy(puzzle)
    
    # Solve Sudoku board
    solution = helpers.solve_sudoku(puzzle)
    
    # Print the original puzzle
    print(colored("\nPUZZLE:", attrs=["bold"]))
    print_puzzle(puzzle)

    # Prompt the user for input and provide options
    while True:
        try:
            user_input = str(input())
            if not validate_user_input(user_input):
                raise ValueError
            if user_input.lower() in ["help", "h"]:
                print_help_message()
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

def print_user_menu():
    """Prints the user menu."""
    table = terminaltables.AsciiTable([
        ["Difficulty", "Description"],
        *[[str(k), v] for k, v in DIFFICULTY_LEVELS.items()]
    ])
    print(table.table)

def get_user_difficulty():
    """Prompts the user to select a difficulty level and returns the selected level."""
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
    return difficulty

def validate_user_input(user_input):
    """
    Validates user input for "help" and "solve" commands.
    Returns True if the input is valid, False otherwise.
    """
    valid_commands = ["help", "solve", "h", "s"]
    return user_input.lower() in valid_commands

def print_help_message():
    """Prints a brief description of the rules of Sudoku."""
    print(colored(
"""
Sudoku is a logic-based number placement puzzle. 
The goal is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 sub-grids contains all of the digits from 1 to 9. 
Each digit can only appear once in each row, column, and sub-grid. 
Good luck!
""", attrs=["blink"]))

def print_puzzle(board):
    """Prints the Sudoku board in a grid format with empty cells represented as '?'."""
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
    """Prints the solved Sudoku board in a grid format with solutions in light green."""
    for i in range(len(solved)):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        for j in range(len(solved[i])):
            if j % 3 == 0:
                print("| ", end="")
            if puzzle[i][j] == 0:
                print(colored(str(solved[i][j]) + " ", "green", attrs=["bold"]), end="")
            else:
                print(str(solved[i][j]) + " ", end="")
            if j == 8:
                print("|")
    print("+-------+-------+-------+")

if __name__ == "__main__":
    main()