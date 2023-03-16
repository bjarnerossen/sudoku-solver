from termcolor import colored

def print_puzzle(board):
    side    = len(board)
    base    = int(side**0.5)
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:]
    line0  = "  "+expandLine("╔═══╤═══╦═══╗")
    line1  = "# "+expandLine("║ . │ . ║ . ║ #")
    line2  = "  "+expandLine("╟───┼───╫───╢")
    line3  = "  "+expandLine("╠═══╪═══╬═══╣")
    line4  = "  "+expandLine("╚═══╧═══╩═══╝")

    symbol = " 123456789" if base <= 3 else " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    nums   = [ [""]+[f"({symbol[-n]})" if n<0 else f" {symbol[n]} "  for n in row]
               for row in board ]
    coord  = "   "+"".join(f" {s}  " for s in symbol[1:side+1])
    lines  = []
    lines.append(coord)
    lines.append(line0)
    for r in range(1,side+1):
        line1n = line1.replace("#",str(symbol[r]))
        lines.append( "".join(n+s for n,s in zip(nums[r-1],line1n.split(" . "))) )
        lines.append([line2,line3,line4][(r%side==0)+(r%base==0)])
    lines.append(coord)
    print(*lines,sep="\n")

def update_puzzle(original, puzzle, x, y):
    side    = len(original)
    base    = int(side**0.5)
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:]
    line0  = "  "+expandLine("╔═══╤═══╦═══╗")
    line1  = "# "+expandLine("║ . │ . ║ . ║ #")
    line2  = "  "+expandLine("╟───┼───╫───╢")
    line3  = "  "+expandLine("╠═══╪═══╬═══╣")
    line4  = "  "+expandLine("╚═══╧═══╩═══╝")

    symbol = " 123456789" if base <= 3 else " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    nums = []
    for i, row in enumerate(original):
        new_row = []
        for j, n in enumerate(row):
            if original[i][j] == 0 and puzzle[i][j] != 0:
                n = puzzle[i][j]
                new_row.append(colored(f" {symbol[n]} ", "green", attrs=["bold"]))
            else:
                new_row.append(f" {symbol[n]} ")
        nums.append([""] + new_row)

    coord  = "   "+"".join(f" {s}  " for s in symbol[1:side+1])
    lines  = []
    lines.append(coord)
    lines.append(line0)
    for r in range(1,side+1):
        line1n = line1.replace("#",str(symbol[r]))
        lines.append( "".join(n+s for n,s in zip(nums[r-1],line1n.split(" . "))) )
        lines.append([line2,line3,line4][(r%side==0)+(r%base==0)])
    lines.append(coord)
    print(*lines,sep="\n")

def print_solution(puzzle, solved):
    side    = len(puzzle)
    base    = int(side**0.5)
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:]
    line0  = "  "+expandLine("╔═══╤═══╦═══╗")
    line1  = "# "+expandLine("║ . │ . ║ . ║ #")
    line2  = "  "+expandLine("╟───┼───╫───╢")
    line3  = "  "+expandLine("╠═══╪═══╬═══╣")
    line4  = "  "+expandLine("╚═══╧═══╩═══╝")

    symbol = " 123456789" if base <= 3 else " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    nums = []
    for i, row in enumerate(puzzle):
        new_row = []
        for j, n in enumerate(row):
            if n == 0:
                n = solved[i][j]
                new_row.append(colored(f" {symbol[n]} ", "green", attrs=["bold"]))
            else:
                new_row.append(f" {symbol[n]} ")
        nums.append([""] + new_row)

    coord  = "   "+"".join(f" {s}  " for s in symbol[1:side+1])
    lines  = []
    lines.append(coord)
    lines.append(line0)
    for r in range(1,side+1):
        line1n = line1.replace("#",str(symbol[r]))
        lines.append( "".join(n+s for n,s in zip(nums[r-1],line1n.split(" . "))) )
        lines.append([line2,line3,line4][(r%side==0)+(r%base==0)])
    lines.append(coord)
    print(*lines,sep="\n")

if __name__ == "__main__":
    pass