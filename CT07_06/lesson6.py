# print("Hello from lesson 6")

# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)
 
# for contact in contacts:
#     for details in contacts:
#         print(details)


students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]


for student in students:
    name, gender = student
    print("Gender of " + name + " is: " + gender)

boys = []
girls = []

for student in students:
    name, gender = student
    if gender == "F":
       girls.append(student)
    if gender == "M":
        boys.append(student)

num_boys = len(boys)
num_girls = len(girls)

print(num_boys)
print(num_girls)

print(boys, girls)


for boy in boys:
    print(boy[0])


