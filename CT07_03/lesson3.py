# print("Hello from lesson 3")

# import time
# study = int(input("How minutes you wanna study? "))

# while (study) != 0 :
#    time.sleep(study*60)
#    study -= 60

# print("Completed ")

import random

num = random.randint(1 , 20)


total_Q = 15
lives = 3 
for i in range(total_Q):
    num = random.randint(2,20)
    num2 = random.randint(2,20)

    while lives>0:
        answer = int(input("What's {num1} x {num2}"))