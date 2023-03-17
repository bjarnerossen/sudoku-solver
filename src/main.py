import terminaltables # Used to print the user menu in a tabular format
from termcolor import colored # Used to colorize output text
import sys # Used to handle keyboard interrupt and exit the program
from copy import deepcopy

# helper functions
import logic # Contains logic to generate and solve Sudoku puzzles
from printer import print_puzzle, print_solution
from game import SudokuGame
from solver import Solver

def main():
    while True:
        print("1. Generate a puzzle")
        print("2. Solve a puzzle")
        print("3. Play a game")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Generate a new Sudoku puzzle board and solve it
            puzzle, solution = logic.generate_sudoku_board()
            original = deepcopy(puzzle)
            print_puzzle(original)
            print_solution(original, solution)

        elif choice == 2:
            solver = Solver()
            solver.solve()
        
        elif choice == 3:
            game = SudokuGame()
            game.play_game()

        elif choice == 4:
            # Quit
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()