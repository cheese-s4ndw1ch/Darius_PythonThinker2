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


pw = input("Please enter password: ")

is_8char_long = True
has_upper = True
has_lower = True
has_num = False
only_alnum = False

if len(pw)>=8:
    is_8char_long = True
for i in pw:
    if i.isupper()==True:
        has_upper == True
for i in pw:
    if i.islower()== True:
        has_lower = True