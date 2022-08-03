# 화성 탐사

import sys
import heapq

input = sys.stdin.readline
t = int(input())
INF = int(1e9)

def solution(t):
    xcor = [0, 0, -1, 1]
    ycor = [-1, 1, 0, 0]
    for _ in range(t):
        n = int(input())
        detectionscope = [list(map(int, input().split())) for _ in range(n)]
        graph = [[INF for _ in range(n)] for _ in range(n)]
        graph[0][0] = detectionscope[0][0]
        q = []
        heapq.heappush(q, (detectionscope[0][0], (0, 0)))
        while q:
            cost, cor = heapq.heappop(q)
            if graph[cor[0]][cor[1]] < cost:
                continue
            for i in range(4):
                y, x = cor[0]+ycor[i], cor[1]+xcor[i]
                if x in ([-1, n]) or y in ([-1, n]):
                    continue
                if cost + detectionscope[y][x] < graph[y][x]:
                    graph[y][x] = cost + detectionscope[y][x]
                    heapq.heappush(q, (cost+detectionscope[y][x], (y, x)))
        print(graph[n-1][n-1])
    
    return

solution(t)
        
    