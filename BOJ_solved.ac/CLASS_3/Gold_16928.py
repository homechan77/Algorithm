# 뱀과 사다리 게임

import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ladder = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
snake ={}
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

visited = [False]*101
visited[1] = True

def bfs():
    queue = deque([(1, 0)])
    while queue:
        x, cnt = queue.popleft()
        if x == 100:
            return cnt
        for i in range(1, 7):
            newx = x+i
            if newx <= 100:    
                if newx in (ladder.keys()):
                    newx = ladder[newx]
                elif newx in (snake.keys()):
                    newx = snake[newx]
                if not visited[newx]:
                    visited[newx] = True
                    queue.append((newx, cnt+1))

print(bfs())
