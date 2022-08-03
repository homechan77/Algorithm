import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
# gate = list(map(lambda x: sorted(x), [list(map(int, input().split())) for _ in range(m)]))
gate = [list(map(int, input().split())) for _ in range(m)]
INF = int(1e9)

def solution(gate):
    distance = [INF for _ in range(n+1)]
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue
        for i in gate:
            if i[0] == node:
                if cost + 1 < distance[i[1]]:
                    distance[i[1]] = cost + 1
                    heapq.heappush(q, (distance[i[1]], i[1]))
            elif i[1] == node:
                if cost + 1 < distance[i[0]]:
                    distance[i[0]] = cost + 1
                    heapq.heappush(q, (distance[i[0]], i[0]))
    
    answer = [0, 0, 0]
    for a in range(1, n+1):
        if answer[1] < distance[a]:
            answer[0], answer[1], answer[2] = a, distance[a], 1
        elif answer[1] == distance[a]:
            answer[2] += 1
    print(" ".join(map(lambda x: str(x), answer)))           

solution(gate)

# 입력 예제
# 4 2 3
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
#result: 4 2 3
