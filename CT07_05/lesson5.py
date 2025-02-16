print("Hello from lesson 5")

import random

counter = 0 

lucky_winners = []

while True:

    num = random.randint(1,1000)

    lucky_winners.append(num)

    for num in range(100):

        print(num)

    counter += 1

    if counter >100:

        break