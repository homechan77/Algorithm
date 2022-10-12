# 바이러스

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
pairn = int(input())
pair = [list(map(int, input().split())) for _ in range(pairn)]

pairarr = [[] for _ in range(n+1)]
for i in pair:
    a, b = i
    pairarr[a].append(b)
    pairarr[b].append(a)


def bfs(pairarr):
    visited = [0]*(n+1)

    queue = deque([])
    queue.extend(pairarr[1])

    while queue:
        pop = queue.popleft()
        if visited[pop] != 1:
            visited[pop] = 1
            queue.extend(pairarr[pop])
    return visited

result = bfs(pairarr)
answer = sum(result[2:])
print(answer)