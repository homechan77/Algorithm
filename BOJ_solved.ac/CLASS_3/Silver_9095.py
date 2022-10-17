# 1, 2, 3 더하기
'''
# BFS 활용
import sys; input = sys.stdin.readline
from collections import deque

t = int(input())

def bfs(n):
    global cnt

    queue = deque([])
    for i in [1, 2, 3]:
        if n - i >= 0:
            queue.append(n-i)
    while queue:
        pop = queue.popleft()
        if pop == 0:
            cnt += 1
            continue
        for i in [1, 2, 3]:
            if pop - i >= 0:
                queue.append(pop-i)

for _ in range(t):
    n = int(input())
    cnt = 0
    bfs(n)
    print(cnt)
'''

##--------------------------------------------------------------------------##
# DP 점화식 활용

import sys; input = sys.stdin.readline
from collections import deque

t = int(input())

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for _ in range(t):
    n = int(input())
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])

