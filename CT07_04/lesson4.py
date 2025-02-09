print("Hello from lesson 4")

Planets = ["Mercury" , "Venus" , "Earth" , "Mars" , "Jupiter" , "Saturn" , "Uranus" , "Neptune"]


print(Planets[3])
Planets[3] = "Gyat Prime"
print(Planets[3])
print(len(Planets))
for counter in range(len(Planets)):
    print(Planets[counter])

Planets.insert(3, "Jawline Land")