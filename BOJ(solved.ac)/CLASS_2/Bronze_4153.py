import sys

nlist = []
while True:
    a = list(map(int, sys.stdin.readline().split()))
    if a == [0,0,0]:
        break
    nlist.append(a)

def solution(nlist):
    for i in nlist:
        i = sorted(i, reverse=False)
        if (i[0]**2)+(i[1]**2) == i[2]**2:
            print('right')
        else:
            print('wrong')

solution(nlist)