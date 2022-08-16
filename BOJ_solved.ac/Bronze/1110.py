a = input()
b = list(a)
if int(a) < 10:
    b.insert(0, 0)
c = int(a)
count = 0
while True:
    suma = int(b[0]) + int(b[1])
    c = int(b[1] + str(suma%10))
    count += 1
    if c == int(a):
        break
    if c < 10:
        c = int(str(c)*2)
        count += 1
        if c == int(a):
            break
    b = list(str(c))
print(count)