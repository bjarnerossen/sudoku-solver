# Third party
from copy import deepcopy # Used to create a deep copy of the Sudoku board
from termcolor import colored # Used to colorize output text
import terminaltables # Used to print the user menu in a tabular format
import datetime

# Own files
import helpers # Contains helper functions to generate and solve Sudoku puzzles

# Libraries to generate pdf
from reportlab.pdfgen import canvas # Used to create PDF documents
from reportlab.lib.pagesizes import letter # Used to set the page size for PDF documents
from reportlab.lib.units import inch # Used to set the measurement unit for PDF documents


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

    # Get user input for number of Sudokus to generate
    num_sudokus = get_num_sudokus()

    # Initialize the PDF document
    c = canvas.Canvas(f"{datetime.date.today()}-{DIFFICULTY_LEVELS[difficulty]}-sudokus.pdf", pagesize=letter)

    # Set the title of the PDF document
    c.setTitle("Sudoku Puzzles")

    # Print the cover page
    c.setFont("Helvetica-Bold", 24)
    c.drawString(inch, 10*inch, "Sudoku Puzzles")
    c.setFont("Helvetica", 14)
    c.drawString(inch, 9*inch, f"Difficulty Level: {DIFFICULTY_LEVELS[difficulty]}")
    c.drawString(inch, 8*inch, f"Number of Sudokus: {num_sudokus}")
    c.showPage()

    # Generate the Sudokus and store the puzzles and solutions in lists
    puzzles = []
    solutions = []
    for i in range(1, num_sudokus+1):
        # Generate Sudoku board and its copy
        puzzle = helpers.generate_sudoku_board(difficulty)
        puzzle_copy = deepcopy(puzzle)

        # Solve Sudoku board
        solution = helpers.solve_sudoku(puzzle)

        # Add the puzzle and solution to the lists
        puzzles.append(puzzle)
        solutions.append(solution)

        # Print the original puzzle on the PDF document
        if i % 2 == 1:
            # Top half of the page
            x = 2.25 * inch
            y = 9.5 * inch - (i//2 * 2.25 * inch)
        else:
            # Bottom half of the page
            x = 5.75 * inch
            y = 9.5 * inch - (i//2 - 1) * 2.25 * inch
        print_puzzle_to_pdf(c, puzzle_copy, x, y)

        # Print progress
        print(f"Generated {i}/{num_sudokus} Sudokus")

        # If we've printed two puzzles, move to the next page
        if i % 2 == 0:
            c.showPage()

    # Save the PDF document
    c.save()

    # Print confirmation message
    print(f"\nSudokus generated and saved to 'sudokus.pdf'")
    
def print_user_menu():
    # Define the user menu as a list of tuples
    menu = [
    ("1", "Easy"),
    ("2", "Medium"),
    ("3", "Intermediate"),
    ("4", "Extreme")
    ]
    # Define the table headers
    headers = ["Difficulty Level", "Description"]
    
    # Create a table object with the menu and headers
    table = terminaltables.AsciiTable([headers] + menu)
    
    # Print the table to the console
    print(table.table)

def get_user_difficulty():
    # Get user input for difficulty level
    while True:
        try:
            difficulty = int(input("Enter the difficulty level (1-4): "))
            if difficulty in range(1,5):
                return difficulty
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


def get_num_sudokus():
    # Get user input for number of Sudokus to generate
    while True:
        try:
            num_sudokus = int(input("Enter the number of Sudokus to generate: "))
            # Check if the input is positive
            if 0 < num_sudokus < 20:
                return num_sudokus
            else:
                print("Invalid input. Please enter a positive number less than 20.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            
def print_puzzle_to_pdf(c, puzzle, x, y):
    # Define the font for the Sudoku puzzle
    c.setFont("Helvetica-Bold", 18)

    # Loop over the rows and columns of the puzzle and print the values
    for row in range(9):
        for col in range(9):
            # Determine the color of the value (black for given values, red for empty values)
            color = "black" if puzzle[row][col] != 0 else "red"
    
            # Print the value with the appropriate color at the appropriate position
            c.setFillColor(color)
            c.drawString(x + col * 0.4 * inch, y - row * 0.4 * inch, str(puzzle[row][col]))
    

def print_solution_to_pdf(c, puzzle, solution, x, y):
    # Print the label for the solution
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y - 0.25 * inch, "Solution:")

    # Set the color of the text to green for the solved cells
    c.setFont("Helvetica", 12)
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                c.setFillColorRGB(0, 0.6, 0)
                c.drawString(x + col * 0.35 * inch, y - (row + 1) * 0.35 * inch, str(solution[row][col]))
                c.setFillColorRGB(0, 0, 0)

    # Draw the horizontal and vertical lines
    for i in range(10):
        if i % 3 == 0:
            c.setLineWidth(2)
        else:
            c.setLineWidth(1)
        c.line(x, y - i * 0.35 * inch, x + 2.8 * inch, y - i * 0.35 * inch)
        c.line(x + i * 0.35 * inch, y, x + i * 0.35 * inch, y - 2.8 * inch)

    # Draw the borders
    c.setLineWidth(2)
    c.line(x, y, x + 2.8 * inch, y)
    c.line(x, y - 2.8 * inch, x + 2.8 * inch, y - 2.8 * inch)
    c.line(x, y, x, y - 2.8 * inch)
    c.line(x + 2.8 * inch, y, x + 2.8 * inch, y - 2.8 * inch)

    # Move to the next position
    if x == 3 * inch:
        c.showPage()
        x = 0.5 * inch
        y -= 3 * inch
    else:
        x += 3 * inch

# def print_puzzle(board):
#     """Prints the Sudoku board in a grid format with empty cells represented as '?'."""
#     for i in range(len(board)):
#         if i % 3 == 0:
#             print("+-------+-------+-------+")
#         for j in range(len(board[i])):
#             if j % 3 == 0:
#                 print("| ", end="")
#             if board[i][j] == 0:
#                 print(colored("?", "white", "on_black", attrs=["bold"]) + " ", end="")
#             else:
#                 print(str(board[i][j]) + " ", end="")
#             if j == 8:
#                 print("|")
#     print("+-------+-------+-------+")

# def print_solution(puzzle, solved):
#     """Prints the solved Sudoku board in a grid format with solutions in light green."""
#     for i in range(len(solved)):
#         if i % 3 == 0:
#             print("+-------+-------+-------+")
#         for j in range(len(solved[i])):
#             if j % 3 == 0:
#                 print("| ", end="")
#             if puzzle[i][j] == 0:
#                 print(colored(str(solved[i][j]) + " ", "green", attrs=["bold"]), end="")
#             else:
#                 print(str(solved[i][j]) + " ", end="")
#             if j == 8:
#                 print("|")
#     print("+-------+-------+-------+")

if __name__ == "__main__":
    main()