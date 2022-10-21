# 좌표 압축

import sys; input = sys.stdin.readline

n = int(input())
xlist = list(map(int, input().split()))
newxlist = list(sorted(set(xlist)))
xdict = {}
for n, i in enumerate(newxlist):
    xdict[i] = n

for j in xlist:
    print(xdict[j], end=' ')
