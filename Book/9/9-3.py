#플로이드 워셜 알고리즘
import numpy as np

INF = int(1e9)

n,m = map(int, input().split()) #노드 개수, 간선 개수
graph = [[INF] * (n+1) for _ in range(n+1)] #2차원 리스트 생성 및 모든 값들을 무한으로 초기화


#출발과 도착이 재귀적인 경우 0으로 설정
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0


#각 노드별 연결된 비용 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

#플로이드 워셔 알고리즘 수행(점화식 활용)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

"""
resultgraph = []
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            graph[a][b] = 'INFINITY'
            resultgraph.append(graph[a][b])
        else:
            resultgraph.append(graph[a][b])

    resultgraph = np.reshape(np.array(resultgraph),(4,4))
    print(resultgraph.shape)
"""
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print() #줄바꿈

