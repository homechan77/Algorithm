# 퇴사(백준_14501)

import sys

input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = [0]*(n+1)
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
max_value = 0

def solution(n, t, p, dp, max_value):
    for i in range(n-1, -1, -1):
        time = t[i] + i
        if time <= n:
            dp[i] = max(p[i]+dp[time], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value
            
    return max_value
    
print(solution(n, t, p, dp, max_value))