


board = []
winning_conditions = [[board[0][0]], [board[0][1]], [board[0][2]], 
                      [board[1][0]], [board[1][1]], [board[1][2]],
                      [board[2][0]], [board[2][1]], [board[2][2]],

                      [board[0][0]], [board[0][1]], [board[0][2]],
                      [board[1][0]], [board[1][1]], [board[1][2]],
                      [board[2][0]], [board[2][1]], [board[2][2]],
                      
                      [board[2][0]], [board[2][0]], [board[2][0]],
                      [board[2][0]], [board[2][0]], [board[2][0]]],

                                                      
                        
                        
                        
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
        

def get_player_move(board):
    move_input = input("Enter your move (1-9): ")
    if move_input.isdigit():
        if int(move_input) >= 0 and int(move_input)  <=9:
            move = int(move_input) - 1
            row = move //3
            col = move % 3
            if board[row][col] == " ":
                board[row][col] = 'X'
            else:
                print("This space is already taken")
        else:
            print("Invalid input! Please enter a value between 1-9.")
    else:
        print("Invalid input! Please enter a number")


board = initialise_board()
while True:




    print_board(board)
    get_player_move(board)
    print_board(board)




















































