list = [36, 54, 6, 52, 99, 38]

        # This script is set to only identify if there's just 1 odd or even
A = []
B = []

for item in list:
    if item % 2 == 0:
        A.append(item)
    else:
        B.append(item)

if len(A) == 1:
    for item in A:
            print(item)
elif len(B) == 1:
    for item in B:
        print(item)
