# ATM

import sys; input = sys.stdin.readline

n = int(input())
p = sorted(list(map(int, input().split())))
dp = [0]*(n+1)

for i, x in enumerate(p):
    dp[i+1] = dp[i] + x

answer = sum(dp)
print(answer)