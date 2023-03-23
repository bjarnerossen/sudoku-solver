import json
from logic import solve_sudoku
from printer import print_solution
from copy import deepcopy
from termcolor import colored
import sys
import inquirer

class Solver:
    def __init__(self):
        pass

    def solve(self):
        # Ask user for input method
        questions = [
            inquirer.List('method',
                    message="How do you want to input the puzzle?",
                    choices=['Text file', 'JSON file'],
                ),
        ]
        answers = inquirer.prompt(questions)

        if answers is None:
            sys.exit(1)

        # Get the input file from the user
        if answers['method'] == 'Text file':
            extension = 'txt'
        else:
            extension = 'json'
        
        filename = input(f"Enter the {extension} file name: ")
        if filename is None:
            sys.exit(1)
        path = f"puzzle/{filename}"
        
        # Read the file
        try:
            with open(path, 'r') as file:
                if extension == 'txt':
                    # Read the text file
                    puzzle = [[int(num) for num in line.split()] for line in file.readlines()]
                    original = deepcopy(puzzle)

                else:
                    # Read the JSON file
                    data = json.load(file)
                    puzzle = data['grid']
                    original = deepcopy(puzzle)
        
                # Check the validity of the puzzle
                if len(puzzle) != 9 or any(len(row) != 9 for row in puzzle) or any(num not in range(10) for row in puzzle for num in row):
                    raise ValueError(colored("Invalid puzzle format or values.", "yellow"))
        
                # Solve the puzzle
                solution = solve_sudoku(puzzle)

                # Check if the puzzle is solvable
                if solution is None:
                    raise ValueError(colored("The puzzle is not solvable.", "red"))

                # Print the solution
                print_solution(original, solution)
        
        except FileNotFoundError:
            print("File not found.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except KeyboardInterrupt:
            sys.exit(1)

if __name__ == "__main__":
    solver = Solver()
    solver.solve()
