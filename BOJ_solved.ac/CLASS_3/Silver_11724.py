# 연결 요소의 개수

import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

visited = [False] * (n+1)

inter = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    inter[u].append(v)
    inter[v].append(u)
    
cnt = 0
for i in range(1, n+1):
    if visited[i] == True:
        continue
    visited[i] = True
    queue = deque(inter[i])
    while queue:
        pop = queue.popleft()
        if visited[pop] == True:
            continue
        visited[pop] = True
        for j in inter[pop]:
            if visited[j] == False:
                queue.append(j)
    cnt += 1

print(cnt)