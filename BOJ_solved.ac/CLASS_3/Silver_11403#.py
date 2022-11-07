# 경로 찾기

import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
infolist = [[] for _ in range(n+1)]
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j, x in enumerate(temp):
        if x == 1:
            infolist[i+1].append(j+1)

result = []
for i in arr:
    queue = deque([])
    visited = [0] * (n+1)
    for j, x in enumerate(i):
        if x == 1:
            queue.append(j+1)
    while queue:
        pop = queue.popleft()
        visited[pop] = 1
        for k in infolist[pop]:
            if visited[k] != 1:
                queue.append(k)
    print(' '.join(map(lambda x: str(x), visited[1:])))

"""
# 플로이드워셜 적용
import sys

input = sys.stdin.readline
N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j]=1

for r in graph:
    for c in r:
        print(c, end = " ")
    print()
"""