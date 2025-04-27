print("Hello from lesson 11_12_13")


board = []

def initialise_board():
    
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)

    return board

cell_number = 1

def print_board(board):
    print("\nBoard Layout: ")
    cell_number = 1
    for row in board:
        for cell in row:
            if cell != ' ':
                print(" " + str(cell) + " " , end="")
            else:
                print(" " + str(cell_number) + " ", end="")
            if cell_number % 3 !=0:
                print("|", end="")
            cell_number += 1

        if (cell_number) <=9:
            print("\n-----------")
    print("\n")
        

def get_player_move():
    move_input = input("Enter your move (1-9): ")
    move = int(move_input) - 1
    row = move //3
    col = move % 3
    



print(initialise_board()) 
print_board(board)

