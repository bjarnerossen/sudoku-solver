# 3rd party
from termcolor import colored
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

    def __init__(self):
        self.original = None
        self.puzzle = None
        self.solution = None
        self.score = 0
        self.tries = 0
        self.game = True

    def play_game(self):
        level = self.choose_difficulty_level()
        self.puzzle, self.solution = logic.generate_sudoku_board(level)
        self.original = deepcopy(self.puzzle)
        start_time = time.time()  # record start time

        # Print the initial board for the given level of difficulty
        print_puzzle(self.puzzle)

        while self.game:
            # Prompt the user for input and provide options
            try:
                x = int(input(colored("x: ", attrs=["bold"]))) 
                y = int(input(colored("y: ", attrs=["bold"])))
                if x not in self.VALID_NUMS or y not in self.VALID_NUMS:
                    raise ValueError
                elif self.original[x-1][y-1] != 0:
                    print(colored("cell already solved", "red"))
                    pass
                else:
                    x = x-1
                    y = y-1
                    num_guess = int(input(colored("num: ", attrs=["bold"])))
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
                            self.game = False
                        else:
                            self.game = True

            except ValueError:
                    print("enter valid number")
            except KeyboardInterrupt:
                sys.exit()

        end_time = time.time()  # record end time
        time_elapsed = end_time - start_time
        print(colored("solved", "green", attrs=["bold"]) + f"Score: {self.score}    Tries: {self.tries}" + colored(f"    Time elapsed: {helpers.format_time(time_elapsed)}", attrs=["bold"]))
        return False

    def choose_difficulty_level(self):
        while True:
            try:
                level = int(input("Choose a difficulty level (1 for easy, 2 for medium, 3 for hard, 4 for extreme): "))
                if level not in [1, 2, 3, 4]:
                    raise ValueError
                return level
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

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