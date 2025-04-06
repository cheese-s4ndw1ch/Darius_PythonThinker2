# print("Hello from lesson 9")
# riddle = input("Type ze riddle: ")

# isCorrect = False
# lowercase = riddle.lower()
# riddle_split = lowercase.split()
# for word in riddle_split:
#     if word == "egg":
#         isCorrect = True
# if isCorrect: 
#     print("Correct! Well done!")
# else:
#     print("Wrong! Try again nuthead!")

import turtle
import random

window = turtle.Screen()
window.setup(600,600)
window.bgcolor("forestgreen")


pen = turtle.Turtle()
pen.penup()
pen.shape("square")
pen.sety(250)


for i in range(-600,600,25):
    pen.setx(i)
    pen.stamp()


pen.goto(-300,-250)
pen.pencolor("yellow")
pen.down()
pen.seth(0)
pen.forward(600)
pen.hideturtle()


gay = turtle.Turtle()
gay.penup()
gay.seth(90)
gay.shape("turtle")
gay.color("red")
gay.goto(0, -250)
gay.write("gay", align = "center", font=('Arial', 20))

sigma = turtle.Turtle()
sigma.penup()
sigma.seth(90)
sigma.shape("turtle")
sigma.color("blue")
sigma.goto(-200, -250)
sigma.write("sigma", align = "center", font=('Sarpanch', 20))



skibidi = turtle.Turtle()
skibidi.penup()
skibidi.seth(90)
skibidi.shape("turtle")
skibidi.color("white")
skibidi.goto(200, -250)
skibidi.write("skibidi", align = "center", font=('Sarpanch', 20))


winner = ""


ask = input("Who shall wins?")


gay.pendown()
random.randint()























window.mainloop()


