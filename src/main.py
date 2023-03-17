from termcolor import colored
from copy import deepcopy
import sys
import inquirer

import logic
from printer import print_puzzle, print_solution
from game import SudokuGame
from solver import Solver

def main():
    menu_choices = [
        inquirer.List('menu_choice',
                      message="What would you like to do?",
                      choices=[
                          ('Generate a puzzle', 'generate'),
                          ('Solve a puzzle', 'solve'),
                          ('Play a game', 'play'),
                          ('Quit', 'quit'),
                      ],
        )
    ]

    while True:
        answers = inquirer.prompt(menu_choices)

        if answers is None or answers['menu_choice'] == 'quit':
            # Quit
            break

        elif answers['menu_choice'] == 'generate':
            # Generate a new Sudoku puzzle board and solve it
            puzzle, solution = logic.generate_sudoku_board()
            original = deepcopy(puzzle)
            print_puzzle(original)
            print_solution(original, solution)

        elif answers['menu_choice'] == 'solve':
            solver = Solver()
            solver.solve()

        elif answers['menu_choice'] == 'play':
            game = SudokuGame()
            game.play_game()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()