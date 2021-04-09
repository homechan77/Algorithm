a = list(str(sum(list(map(int, input().split())))))[::-1]
a = list(map(int, a))
newlist = [0]*len(a)
for i in range(len(a)):
    if a[i] >= 2:
        newlist[i] = a[i]-2
        if i == len(a)-1:
            newlist.append(1)
        else:
            a[i+1] += 1
    else:
        newlist[i] = a[i]

n = 0
for j in range(len(newlist)):
    n += newlist[j] * (10**j)
print(n)