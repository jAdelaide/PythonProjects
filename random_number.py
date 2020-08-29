#
#Bananas = 5
import random
Bananas = (random.randint(0,10))
#
#print("If I have 5 or more bananas, my bunch is large.\
#        Else if I have 1-4 bananas, my bunch is small.\
#        Else: I don't have any bananas.")
print()
print("Number of bananas:  " + str(Bananas))
print()
if int(Bananas) > 4:
    print("Oh my gosh, Becky, lookkat. her. bunch.")
elif 0 < int(Bananas) < 5:
    print("Goddamn, what a little bunch")
else:
    print("Where are my bananas?")
