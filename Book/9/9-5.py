import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

"""
result = []
for i in range(1, n+1):
    if distance[i] == INF:
        result.append('INFINITY')
    else:
        result.append(distance[i])

print(m, max(result))
"""
#해설참조
# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)

            