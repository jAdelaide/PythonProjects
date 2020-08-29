Start = input("Where do you want to start counting from?\n")
    # Change Start to start counting from different points
Range = input("And how many numbers do you want to count?\n")
    # Choose how far it counts

print()
print(Start)

Counter = int(Start) + 1

while Counter < int(Start) + int(Range):
    print(Counter)
    Counter = int(Counter) + 1

if Counter >= int(Start) + int(Range):
    print(Counter)
    print()
    print("Counted " + str(Range) + " numbers, from " + str(Start) + " to " + str(Counter) + "!")
