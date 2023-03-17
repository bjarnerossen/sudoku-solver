# 3rd party
from termcolor import colored
import inquirer

# Built-in
import sys 
import time
from copy import deepcopy
# Own functions
import logic
import helpers
from printer import print_puzzle, print_updated_puzzle

class SudokuGame:
    VALID_NUMS = [1,2,3,4,5,6,7,8,9]

    LEVEL_CHOICES = [
        ('Easy', '1'),
        ('Medium', '2'),
        ('Hard', '3'),
        ('Extreme', '4')
    ]

    def __init__(self):
        self.original = None
        self.puzzle = None
        self.solution = None
        self.score = 0
        self.tries = 0
        self.game = True

    def play_game(self):
        questions = [
            inquirer.List('level',
                          message="Choose a difficulty level",
                          choices=self.LEVEL_CHOICES,
            )
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            sys.exit(1)
        level = int(answers['level'])
        self.puzzle, self.solution = logic.generate_sudoku_board(level)
        self.original = deepcopy(self.puzzle)
        start_time = time.time()  # record start time

        # Print the initial board for the given level of difficulty
        print_puzzle(self.puzzle)

        while self.game:
    # Prompt the user for input and provide options
            try:
                VALID_NUMS = [1,2,3,4,5,6,7,8,9]
                questions = [
                    inquirer.Text('cell', message="Enter the cell coordinates (x, y)"),
                ]
                answers = inquirer.prompt(questions)
                if answers is None:
                    sys.exit(1)
                try:
                    x, y = map(int, answers['cell'].split(','))
                    if x not in VALID_NUMS or y not in VALID_NUMS:
                        print(colored("Invalid coordinates. Enter coordinates between 1 and 9 inclusive", "red"))
                        continue
                except ValueError:
                    print(colored("Invalid input. Enter x and y values separated by comma (,)", "red"))
                    continue
        
                # Check if cell is already solved
                if self.original[x-1][y-1] != 0:
                    print(colored("cell already solved", "red"))
                    continue
        
                # Prompt user for number to fill the cell
                questions = [
                    inquirer.Text('num', message=f"Enter the number for cell ({x}, {y}):", validate=lambda _, n: n.isdigit() and int(n) in VALID_NUMS)
                ]
                answers = inquirer.prompt(questions)
                if answers is None:
                    sys.exit(1)
                num_guess = int(answers['num'])

                x = x-1
                y = y-1
                self.tries += 1
                check_answer = self.is_correct_answer(num_guess, x, y)
                if not check_answer:
                    print_puzzle(self.original)
                    if self.score > 0:
                        self.score -= 1
                        print(colored("wrong num", "red"))
                        end_time = time.time()  # record end time
                        time_elapsed = end_time - start_time
                        print(colored(f"Score: {self.score}", attrs=["bold"]) + colored("   -1", "red", attrs=["bold"]) + colored(f"    Tries: {self.tries}", attrs=["bold"]) + colored(f"    Time elapsed: {helpers.format_time(time_elapsed)}", attrs=["bold"]))
                    else:
                        print(colored("wrong num", "red"))
                        end_time = time.time()  # record end time
                        time_elapsed = end_time - start_time
                        print(colored(f"Score: {self.score}", attrs=["bold"]) + colored(f"    Tries: {self.tries}", attrs=["bold"]) + colored(f"    Time elapsed: {helpers.format_time(time_elapsed)}", attrs=["bold"]))
                        pass
                    self.game = True
                else:
                    self.original[x][y] = int(num_guess)
                    self.score += 1
                    print_updated_puzzle(self.puzzle, self.original, x, y)
                    print(colored("correct num", "green"))
                    end_time = time.time()  # record end time
                    time_elapsed = end_time - start_time
                    print(colored(f"Score: {self.score}", attrs=["bold"]) + colored("   +1", "green", attrs=["bold"])+ colored(f"    Tries: {self.tries}", attrs=["bold"])+ colored(f"    Time elapsed: {helpers.format_time(time_elapsed)}", attrs=["bold"])
                        )

                    # find the first empty cell
                    row, _ = logic.find_empty_cell(self.original)
                 
                    # if no empty cell is found, the sudoku is solved
                    if row == -1:
                        print(colored("Congratulations, you solve the sudoku!", "green"))
                        self.game = False
                    else:
                        self.game = True

            except ValueError:
                    print("enter valid number")
            except KeyboardInterrupt:
                sys.exit(1)

        end_time = time.time()  # record end time
        time_elapsed = end_time - start_time
        print(colored("solved", "green", attrs=["bold"]) + f"Score: {self.score}    Tries: {self.tries}" + colored(f"    Time elapsed: {helpers.format_time(time_elapsed)}", attrs=["bold"]))
        return False

    def generate_puzzle(self, level):
        self.puzzle = logic.generate_sudoku_board(level)
        self.original = deepcopy(self.puzzle)

    def solve_puzzle(self):
        self.solution = logic.solve_sudoku(self.puzzle)

    def is_correct_answer(self, num_guess, x, y):
        if int(num_guess) == int(self.solution[x][y]):
            return True
        else:
            return False

if __name__ == "__main__":
    game = SudokuGame()
    game.play_game()