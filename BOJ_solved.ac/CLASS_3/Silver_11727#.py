# 2×n 타일링 2

import sys; input = sys.stdin.readline

n = int(input())

def solution(n):
    if n == 1:
        return 1
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]*2
    return dp[n] % 10007

print(solution(n))