# 국영수(백준_10825)

import sys
input = sys.stdin.readline

n = int(input())
nlist = [list(input().split()) for _ in range(n)]

def solution(nlist):
    nlist = sorted(nlist, key=lambda x: [(-int(x[1]),int(x[2]),-int(x[3]), x[0])])
    for i in nlist:
        print(i[0])
        
solution(nlist)