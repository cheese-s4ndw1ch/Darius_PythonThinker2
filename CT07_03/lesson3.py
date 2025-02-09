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
    num1 = random.randint(2,20)
    num2 = random.randint(2,20)
    correct = num1 * num2

    while lives>0:
        answer = int(input("What's {num1} x {num2}"))

        if answer == correct:
            print("Nice! Don't mess up the next one! Ơ̸̢̢̤̙̠̘̣͓̤̝̻̙̓̐͛̏̀̒͝ͅŘ̸̨̡̥̙̰̯̼̪̰̠͖̬̙͓͍̊̐̑̇̋̔̇̑͘ ̷̡̢̛̲͙̰̣̉̀̒Ẽ̶̡̮̭͈̙̙̻͉̬̗̺̜̤̣͒̾L̸̢̯͙͚̼͇͖̰̹̓̌̈́̀̀̉̅̉̒Ș̶̨̖̗̘̠͕̩̼͕̄̓̇͐͗̅̎̀̈́̕͠͝ͅȨ̵̥̝͐̋́̊̋͝")
            break
        else:
            lives -= 1
            
   