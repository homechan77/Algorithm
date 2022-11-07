# 동전 0

import sys; input = sys.stdin.readline

n, k = map(int, input().split())
nlist = sorted([int(input()) for _ in range(n)], reverse=True)

def solution(k):
    result = 0
    for i in nlist:
        if i <= k:
            result += (k//i)
            k %= i
        if k == 0:
            return result

print(solution(k))