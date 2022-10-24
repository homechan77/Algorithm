# 단지번호붙이기

import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
map = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# up, down, left, right
xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0]

def bfs(row, col):
    global n

    cnt = 0
    queue = deque([(row, col)])
    while queue:
        pop = queue.popleft()
        cnt += 1
        r, c = pop[0], pop[1]
        for i in range(4):
            new_r, new_c = r+ycor[i], c+xcor[i]
            if new_r not in [-1, n] and new_c not in [-1, n]:
                if not visited[new_r][new_c]:
                    if map[new_r][new_c] == '1':
                        visited[new_r][new_c] = True
                        queue.append((new_r, new_c))
                    else:
                        visited[new_r][new_c] == True
    return cnt

def solution(n):
    result = []
    for i in range(n):
        for j in range(n):
            if map[i][j] == '1':
                if not visited[i][j]:
                    visited[i][j] = True
                    result.append(bfs(i, j))
            else:
                visited[i][j] = True
    result.sort()
    print(len(result))
    for a in result:
        print(a)

solution(n)