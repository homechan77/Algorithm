array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
list = [0] * (max(array)+1)

for i in array:
    list[i] += 1

for j in range(len(list)):
    for k in range(list[j]):
        print(j, end = ' ')