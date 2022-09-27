# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(n):
    global k
    
    visited = [False]*(100000+1)

    queue = deque([(n, 0)])

    while queue:
        pop = queue.popleft()
        point, result = pop[0], pop[1]
        visited[point] = True
        if point == k:
            return result
        plist = [point-1, point+1, point*2]
        for i in plist:
            if (0 <= i <= 100000) and not visited[i]:
                queue.append((i, result+1))
    
def solution(n):
    answer = bfs(n)
    return answer

print(solution(n))