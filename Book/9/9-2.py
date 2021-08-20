#다익스트라 알고리즘2(우선순위 큐를 활용한 개선된 다익스트라 알고리즘)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split()) #노드개수, 간선개수
start = int(input()) #시작노드 설정
graph = [[] for i in range(n+1)] #인덱스와 노드 번호 일치를 위한 (n+1)
distance = [INF] * (n+1) #최단거리 테이블을 무한으로 초기화

#모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #a번 노드에서 b번 노드로 가는 비용 c

def ndijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #시작 노드로 가기 위한 최단경로는 0으로 설정, 큐에 삽입
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

ndijkstra(start)

result = []
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        result.append(distance[i])

print(result)
