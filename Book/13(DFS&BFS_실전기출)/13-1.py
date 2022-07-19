# 특정 거리의 도시 찾기
# 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력
##--------------------------------------------------------------------------##
import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
mlist = [list(map(int, input().split())) for _ in range(m)]
INF = int(1e9)

def solution(n, k, x, mlist):
    graph = [[] for _ in range(n+1)]
    for i in mlist:
        graph[i[0]].append(i[1])
        
    visited = [INF]*(n+1)
    visited[x] = 0
    queue = deque([x])
    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if visited[pop]+1 < visited[i]:
                visited[i] = visited[pop]+1
                queue.append(i)

    alarm = False
    for i in range(len(visited)):
        if visited[i] == k:
            alarm = True
            print(i)
    if alarm is False:
        print(-1)
        
solution(n, k, x, mlist)

