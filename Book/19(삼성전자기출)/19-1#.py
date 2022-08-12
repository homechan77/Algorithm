# 아기 상어(백준_16236)
# bfs를 이용한 최단 거리 계산

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)

def bfs(n, space, y_now, x_now, size):
    xcor = [0, 0, -1, 1]
    ycor = [-1, 1, 0, 0]
    dist = [[-1]*n for _ in range(n)]
    dist[y_now][x_now] = 0
    queue = deque([(y_now, x_now)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yi = y + ycor[i]
            xi = x + xcor[i]
            if (xi not in ([n, -1])) and (yi not in ([n, -1])):
                if dist[yi][xi] == -1 and space[yi][xi] <= size:
                    dist[yi][xi] = dist[y][x] + 1
                    queue.append((yi, xi))
    return dist

def find(dist, space, size):
    y, x = 0, 0
    minn = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] > -1 and 1 <= space[i][j] and space[i][j] < size:
                if dist[i][j] < minn:
                    y, x = i, j
                    minn = dist[i][j]
    if minn == INF:
        return None
    else:
        return y, x, minn
                
def solution(n, space):
    size_now = 2
    y_now, x_now = 0, 0
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                y_now, x_now = i, j
                space[y_now][x_now] = 0
    
    answer = 0
    ate = 0
    while True:
        # dist = bfs(n, space, y_now, x_now, size_now)
        value = find(bfs(n, space, y_now, x_now, size_now), space, size_now)
        if value == None:
            print(answer)
            break
        else:
            y_now, x_now = value[0], value[1]
            answer += value[2]
            space[y_now][x_now] = 0
            ate += 1
            if ate >= size_now:
                size_now += 1
                ate = 0
    
solution(n, space)

#test_linux
