from termcolor import colored
import sys 
from copy import deepcopy
import helpers
from printer import print_puzzle, print_solution, update_puzzle

def play_game(puzzle, solution):
    VALID_NUMS = [1,2,3,4,5,6,7,8,9]
    original = puzzle
    puzzle = deepcopy(original)
    score = 0
    game = True
    while game:
        # Prompt the user for input and provide options
        try:
            x, y = int(input(colored("x: ", attrs=["bold"]))), int(input(colored("y: ", attrs=["bold"])))
            if x not in VALID_NUMS or y not in VALID_NUMS:
                raise ValueError
            else:
                x = x-1
                y = y-1
                num_guess = int(input(colored("num: ", attrs=["bold"])))
                check_answer = is_correct_answer(num_guess, x, y, solution)
                if not check_answer:
                    if score > 0:
                        score -= 1
                    else:
                        pass
                    print("wrong num")
                    print("Score: " + colored(f"{score}", attrs=["bold"]) + colored("   -1", "red", attrs=["bold"]))
                    game = True
                else:
                    original[x][y] = int(num_guess)
                    score += 1
                    print(colored("correct num", "green"))
                    print("Score: " + colored(f"{score}", attrs=["bold"]) + colored("   +1", "green", attrs=["bold"]))
                    update_puzzle(puzzle, original, x, y)
                    # find the first empty cell
                    row, _ = helpers.find_empty_cell(puzzle)
                 
                    # if no empty cell is found, the sudoku is solved
                    if row == -1:
                        game = False
                    else:
                        game = True

        except ValueError:
                print("enter valid number")
        except KeyboardInterrupt:
            sys.exit()

    return False
    
def is_correct_answer(num_guess, x, y, solution):
    if int(num_guess) == int(solution[x][y]):
        return True
    else:
        return False