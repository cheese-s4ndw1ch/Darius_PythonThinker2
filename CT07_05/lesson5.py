print("Hello from lesson 5")

#import random

#counter = 0 

#lucky_winners = []

#while True:

    #num = random.randint(1,1000)

    #lucky_winners.append(num)

    #for num in range(100):

        #print(num)

    #counter += 1

    #if counter >100:

        #break


namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
            "Sophia", "Lucas", "Mia", "Aiden"
            ]
heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

tallest = max(heightlist)
shortest = min(heightlist)

print (tallest)
print(namelist[heightlist.index](tallest))

print(shortest)
print(namelist[heightlist.index](tallest))