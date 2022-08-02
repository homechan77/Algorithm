# 정확한 순위

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]

INF = int(1e9)

def solution(n, array):
    # 플로이드 워셜 알고리즘을 사용하여 두 노드간 직접적 연결 혹은 간접적 연결 여부 상관없이 연결 현황을 파악한다.
    # graph 안의 숫자는 i노드(출발)와 j노드(도착)가 몇 번 건너건너 연결되었는지를 알려준다. 
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    for a in array:
        graph[a[0]][a[1]] = 1
    for x in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][x]+graph[x][j])
    
    # graph[i][j] 또는 graph[j][i]가 무한의 수가 아니라는 뜻은 i가 j보다 크거나 또는 작더라도 크기를 비교할 수 있다라는 뜻이기 때문에
    # 나머지 노드와 모두 비교 가능하다면 answer += 1
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                cnt += 1
        if cnt == n:
            answer += 1
    
    return answer

print(solution(n, array))