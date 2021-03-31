a,b = map(int, input().split())
li = []
for _ in range(a):
    line=[]
    for _ in range(b):
        line.append(0)
    li.append(line)
c = int(input())
for _ in range(c):
    d,e,f,g = map(int, input().split())
    if e == 0:
        for x in range(d):
            li[f-1][g-1+x] += 1
    else:
        for y in range(d):
            li[f-1+y][g-1] += 1
for z in li:
    for w in z:
        print(w, end=' ')
    print()