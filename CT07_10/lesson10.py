print("Hello from lesson 10")

# def alert():
#     print("MOTION DETECTED")




# alert()
# alert()
# alert()

# import turtle
# t = turtle.Turtle()

# window = turtle.Screen()

# t.pencolor("black")

# window.bgcolor("white")

# t.pendown()
# t.shape("turtle")

# window.setup(300,300)

# def square(width , height):
#    for _ in range(4):
#       t.forward(height)
#       t.left(90)
      

# square(90,90)




# turtle.mainloop()

import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.setup(300,300)


t.pencolor("black")

window.bgcolor("white")

t.pendown()
t.shape("turtle")


def square(width , height):
    for _ in range(4):
       t.forward(height)
       t.left(90)

square(90,90)


turtle.mainloop()