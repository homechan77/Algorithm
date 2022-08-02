# 플로이드(백준_11404)

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
businformation = [list(map(int, input().split())) for _ in range(m)]

INF = int(1e9)

def floyd_warshall(n, businformation):
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==j:
                graph[i][j] = 0
    for i in businformation:
        a, b, c = i[0], i[1], i[2]
        if graph[a][b] < c:
            continue
        graph[a][b] = c
        
    for x in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][x]+graph[x][j])
    
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] == INF:
                graph[i][j] = 0
                          
    return graph

def solution(n, businformation):
    answergraph = floyd_warshall(n, businformation)
    del answergraph[0]
    for a in answergraph:
        del a[0]
        answer = " ".join(map(lambda x: str(x), a))
        print(answer)

solution(n, businformation)