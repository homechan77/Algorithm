h = input()
hx = h[0]
hy = h[1]

steps = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]

count = 0

for i in steps:
    mx = ord(hx)+i[0]
    my = int(hy)+i[1]
    if mx>104 or mx<97 or my<1 or my>8:
        continue
    count += 1

print(count)
