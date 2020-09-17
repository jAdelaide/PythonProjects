numbers = [1, 2, 3]
target = 4

equals = []
count = 0

if numbers[0] + numbers[1] == target:
    equals = [0, 1]
elif numbers[0] + numbers[2] == target:
    equals = [0, 2]
else:
    equals = [1, 2]


print(equals)

