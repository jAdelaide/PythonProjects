list = [3, 5, 6, 7, 99]

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
