a,b = map(int, input().split())
listn = []
for _ in range(a):
    c = list(map(int, input().split()))
    listn.append(c)
listm = []
for i in range(a):
    listm.append(min(listn[i]))
print(max(listm))