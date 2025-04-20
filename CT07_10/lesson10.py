print("Hello from lesson 10")

# def alert():
#     print("MOTION DETECTED")




# alert()
# alert()
# alert()
import turtle
t = turtle.Turtle()

window = turtle.Screen()

t.pencolor("black")

window.bgcolor("white")

t.pendown()
t.shape("turtle")

window.setup(300,300)

def square(width , height):
    for _ in range(4):
       t.forward(height)
       t.left(90)
      

    square(90,90)




def turtleCoord(turtle_obj):

    x = turtle_obj.xcor()
    y = turtle_obj.ycor()

    return x,y


square(-50,50)

x,y = turtleCoord(t)
print("Turtle coordinates: " + str(x) + str(y))


turtle.mainloop()






turtle.mainloop()



#def elderly():
        #ask = print(input("How old are you?"))
    #if ask <65:
        #print(ask)
        #print("You are eligible for a discount for senior citizens!")
    #else:
        #print(ask)
        #print("You are not eligible for a discount")



import random


def randgen(num):
    
    global number
    number = []
    for i in range(num):
        number = random.randint(1,100)
        number.append(number)
        print(number)




randgen(10)


print("Smallest: " + str(min(number)))
print("Biggest: " + str(max(number)))
avg = sum(number)/len(number)
print("Avg: " + str(avg))









# list_game = ["rock", "paper", "scissors"]
# def generate_computer_move():
#     return random.choice(list_game)

# computer_move = generate_computer_move()
# print("Computer move:" + computer_move)

# player_move = input("Enter your move (rock, paper, scissors): 
# ").lower()

# def determine_winner():
#     if player_move == generate_computer_move:
#         print("Tie!")
# if player_move == "rock":
#     if computer_move == "scissors":
#         print("You won!")
#     else:
#         print("You lose!")
# if player_move == "paper":
#     if computer_move == "rock":
#         print("You won!")
#     else:
#         print("You lose!")
# if player_move == "scissors":
#     if computer_move == "paper":
#         print("You won!")
#     else:
#         print("You lose!")
def initialise_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)


    