li = []
for _ in range(10):
    a = list(map(int, input().split()))
    li.append(a)
b=2
c=2
while True:
    if li[b-1][c-1] == 0:
        li[b-1][c-1] +=9
        c += 1
    elif li[b-1][c-1] == 1:
        b += 1
        c -= 1
    else:
        li[b-1][c-1] +=7
        break
for x in li:
    for y in x:
        print(y, end=' ')
    print()