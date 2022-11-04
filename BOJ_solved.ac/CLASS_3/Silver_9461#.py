# 파도반 수열
# 피보나치 수열

import sys; input = sys.stdin.readline

tn = int(input())

for _ in range(tn):
    pn = int(input())
    if pn < 4:
        print(1)
        continue
    plist = [0]*(pn+1)
    for i in range(1, 4):
        plist[i] = 1
    for j in range(4, pn+1):
        plist[j] = plist[j-2] + plist[j-3]
    print(plist[pn])

