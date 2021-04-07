a = list(input().upper())
b = list(set(a))
c = []
for i in b:
    c.append(a.count(i))
if c.count(max(c)) > 1:
    print('?')
else:
    print(b[c.index(max(c))])