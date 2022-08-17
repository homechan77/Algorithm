# DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split()) # 정점의 개수(n) / 간선의 개수(m) / 시작 정점 번호(v)
conn_info = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for i in conn_info:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
graph = list(map(lambda x: sorted(list(set(x))), graph))

visited_d = [False] * (n+1)
result_dfs = []
def dfs(v):
    result_dfs.append(v)
    visited_d[v] = True
    for i in graph[v]:
        if not visited_d[i]:
            dfs(i)

visited_b = [False] * (n+1)
result_bfs = []
def bfs(v):
    result_bfs.append(v)
    visited_b[v] = True
    queue = deque(graph[v])
    while queue:
        pop = queue.popleft()
        if not visited_b[pop]:
            result_bfs.append(pop)
            visited_b[pop] = True
            for i in graph[pop]:
                if not visited_b[i]:
                    queue.append(i)

dfs(v)
bfs(v)

print(' '.join(map(lambda x: str(x), result_dfs)), ' '.join(map(lambda x: str(x), result_bfs)), sep='\n')