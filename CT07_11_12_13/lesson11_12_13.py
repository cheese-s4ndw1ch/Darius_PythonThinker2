print("Hello from lesson 11_12_13")

def initialise_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)

    return board

cell_number = 1

def print_board():
    print("/nBoard Layout: ")
    cell_number = 1
    for row in board:
        for cell in row:
            print(" " + str(cell) + " " , end="")







print(initialise_board()) 