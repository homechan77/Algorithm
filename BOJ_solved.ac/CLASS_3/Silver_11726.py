# 2×n 타일링

import sys; input = sys.stdin.readline

n = int(input())

def solution(n):
    if n <= 3:
        return n
    result = [0] * (n+1)
    result[1], result[2], result[3] = 1, 2, 3
    for i in range(4, n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n] % 10007

print(solution(n))
