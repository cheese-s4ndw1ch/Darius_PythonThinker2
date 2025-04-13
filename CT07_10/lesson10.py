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
avg 