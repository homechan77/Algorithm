# 치킨 배달

import sys
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]

def solution(n, m, nlist):
    home = defaultdict(int)
    chicken = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if nlist[i][j] == 1:
                home[(i+1,j+1)] = 1
            elif nlist[i][j] == 2:
                chicken[(i+1, j+1)] = 2
    hkeys = list(home.keys())
    ckeys = list(chicken.keys())
    result = [0]*m
    for i in range(m):
        icpy = i+1
        ccombi = list(combinations(ckeys, icpy))
        tmp1 = [0]*len(ccombi)
        for j in range(len(ccombi)):
            for m in hkeys:
                tmp2 = []
                for n in ccombi[j]:
                    tmp2.append(abs(m[0]-n[0])+abs(m[1]-n[1]))
                tmp1[j] += min(tmp2)
        result[i] += min(tmp1)
    
    answer = min(result)
    return answer
    
print(solution(n, m, nlist))
    