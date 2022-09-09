# 1로 만들기

import sys
# from collections import deque

input = sys.stdin.readline
n = int(input())

# 시도1. bfs - 시간초과
# def bfs(n):
#     queue = deque([[n, 0]])
#     while True:
#         pop = queue.popleft()
#         i, cnt = pop[0], pop[1]
#         if i == 1:
#             return cnt
#         if i % 3 == 0:
#             queue.append([i//3, cnt+1])
#         if i % 2 == 0:
#             queue.append([i//2, cnt+1])
#         queue.append([i-1, cnt+1])  


# def solution(n):
#     answer = bfs(n)
#     return answer

# 시도2. bottom-up memoization 
dp = [0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])