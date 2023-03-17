import json
from logic import solve_sudoku
from printer import print_solution
from copy import deepcopy

class Solver:
    def __init__(self):
        pass

    def solve(self):
        # Prompt user for filename
        filename = input("Enter the file name: ")
        
        # Get the input file from the user
        path = f"puzzle/{filename}"
        
        # Read the file
        try:
            with open(path, 'r') as file:
                if filename.endswith('.txt'):
                    # Read the text file
                    puzzle = [[int(num) for num in line.split()] for line in file.readlines()]
                    original = deepcopy(puzzle)

                elif filename.endswith('.json'):
                    # Read the JSON file
                    data = json.load(file)
                    puzzle = data['grid']
                    original = deepcopy(puzzle)
                else:
                    raise ValueError("Invalid file format. Only .txt and .json files are supported.")
        
                # Check the validity of the puzzle
                if len(puzzle) != 9 or any(len(row) != 9 for row in puzzle) or any(num not in range(10) for row in puzzle for num in row):
                    raise ValueError("Invalid puzzle format or values.")
        
                # Check if the puzzle is solvable
                if solve_sudoku(puzzle) is None:
                    raise ValueError("The puzzle is not solvable.")
                
                # Solve the puzzle
                solution = solve_sudoku(puzzle)
        
                # Print the solution
                print_solution(original, solution)
        
        except FileNotFoundError:
            print("File not found.")
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    solver = Solver()
    solver.solve()
