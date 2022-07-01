import sys

n = int(sys.stdin.readline())
nlist = sorted([[sys.stdin.readline().split(), i] for i in range(n)]\
                , key=lambda x: int(x[0][0]))

for j in nlist:
    age = int(j[0][0])
    name = j[0][1]
    print(age, name)
    