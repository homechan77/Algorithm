#프로그래머스 (음식) 배달
#우선순위 큐를 사용한 풀이
#다익스트라 알고리즘

import heapq
INF = int(1e9)

def dijkstra(start, road, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for x in road:
            if x[0] == now:
                cost = dist + x[2]
                next = x[1]
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q, (cost, next))

            elif x[1] == now:
                cost = dist + x[2]
                prev = x[0]
                if cost < distance[prev]:
                    distance[prev] = cost
                    heapq.heappush(q, (cost, prev))
    return distance

def solution(N, road, K):
    answer = 0
    start = 1
    distance = [INF] * (N+1)
    dijkstra(start, road, distance)
    for x in distance:
        if x <= K:
            answer += 1
    return answer


N = 5 #마을 수
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]] #출발마을, 도착마을, 비용(시간)
K = 3 #배달 가능한 비용(시간)

print(solution(N, road, K))