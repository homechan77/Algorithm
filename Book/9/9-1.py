#다익스트라 알고리즘1
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split()) #노드개수, 간선개수

start = int(input()) #시작 노드 번호 입력

graph = [[] for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성

visited = [False] * (n+1) #방문 기록 여부 체크

distance = [INF] * (n+1) #최단거리 테이블을 모두 무한대로 초기화

#모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미


#방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
    


