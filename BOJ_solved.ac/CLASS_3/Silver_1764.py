# 듣보잡

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n, m):
    nlist = set([input().rstrip() for _ in range(n)])
    mlist = set([input().rstrip() for _ in range(m)])
    result = list(nlist.intersection(mlist))
    result.sort(reverse=False)
    print(len(result))
    for i in result:
        print(i)

solution(n, m)