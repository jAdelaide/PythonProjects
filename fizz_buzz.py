print()
        # Input statements set to assign unused variables to wait for a click after          printing text
Start = input(" Let's play Fizz Buzz! (Click enter to continue)")
print()
        # Start game at 1
Click = input("  1")
        # Start counting from 2
Counter = int(2)
        # limit game to 100
while int(Counter) < 101:
        # FIZZ BUZZ
    if int(Counter) % 3 == 0 and int(Counter) % 5 == 0:
        Next = input("  !!! FIZZ BUZZ !!!")
        # Fizz
    elif int(Counter) % 3 == 0:
        Next = input("  Fizz")
        # Buzz
    elif int(Counter) % 5 == 0:
        Next = input("  Buzz")
    else:
        Next = input("  " + str(Counter))
    Counter = int(Counter) + 1
print()
print(" You reached 100!")
print()
