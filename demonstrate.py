Name = input("What is your name?\n")
print()
        # makes sure just 1st name letter is in caps :
print("Hey " + Name.capitalize())
print()
Final = input("Let's make a list, how many items do you want on your list?\n")
if int(Final) > 0:
    print("Great, we'll make a list with " + str(Final) + " values.")
        # list length must be at leat 1 :
elif int(Final) == 0:
    print("We can't make a list with no values!")
    print()
    Final = input("Let's make a list, how many items do you want on your list?\
            \n")
        # if they put a negative number, check if "-" was an accident
else:
    Pos = int(Final) * int(-1)
    Numm = input("The list can't have a negative number of items, did you mean"\
            "\n    " + str(Pos) + "? (y/n)  ")
    if Numm == "y":
     Final = int(Final) * int(-1)
     print("Great, we'll make a list with " + str(Final) + " values.")
    elif Numm == "n":
     Final = input("How many items do you want on your list?\n")
     print("Great, we'll make a list with " + str(Final) + " values.")

        # potential list items
List = ['fruit', 'shower-gel', 'drinks', 'butter', 'bacon', 'eggs', 'sausages','chips', 'crisps', 'chocolate', 'sweets', 'clothes', 'home-decor', 'stationary', 'headphones']

print("\nHere is your list!\n")

        # randomly select items from the list until reaching the specified length
Counter = 0
while int(Counter) < int(Final):
 import random
        # random number between 0 and 14 to relate to the list
 Rand = random.randint(0,14)
 print(List[Rand])
 Counter = int(Counter) + 1

print()

