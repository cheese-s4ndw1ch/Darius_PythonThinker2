# print("Hello from lesson 8")
# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]
# lists = sorted(set(list1 + list2 + list3))

# print(lists)

# mid = len(lists)//2
# right = list[mid:]
# left = list[:mid]
# print(right)
# print(left)


# pw = input("Please create password (Must be more than 8 letters, 1 uppercase + 1 lower case, must have a number): ")

# is_8char_long = True
# has_upper = True
# has_lower = True
# has_num = False
# only_alnum = False

# if len(pw)>=8:
#     is_8char_long = True
# for i in pw:
#     if i.isupper()==True:
#         has_upper = True
# for i in pw:
#     if i.islower()== True:
#         has_lower = True
# for i in pw:
#     if i.isdigit()== True:
#         has_num = True
# if is_8char_long and has_upper and has_lower and has_num == True:
#     print("Password accepted.")
# else:
#     print("Password unacceptable.")





text = input("Type out a random sentence. ")
alt = True
output = ""


for i in text: 
    if alt == True:
        output += i.lower()
        alt == False
    else:
        output += i.upper