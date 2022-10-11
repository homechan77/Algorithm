# 미로 탐색

# 시도 1. 시간 초과
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
# arr2 = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]
result[0][0] = 1

# up, down, left, right
xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0]

def bfs(arr, start):
    queue = deque([start])
    while queue:
        pop = queue.popleft()
        y, x = pop[0], pop[1]
        visited[y][x] = True
        num = result[y][x]
        for i in range(4):
            ny, nx = y+ycor[i], x+xcor[i]
            if ny not in ([-1, n]) and nx not in ([-1, m]):
                if arr[ny][nx] != 0 and visited[ny][nx] == False:
                    queue.append((ny, nx))
                    if result[ny][nx] < num+1:
                        result[ny][nx] = num + 1

def solution(arr):
    bfs(arr, (0, 0))

solution(arr)
# print(result[n-1][m-1])
print(result)
'''
##--------------------------------------------------------------------------##
# 시도 2.
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
# arr2 = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
result = [[0] * m for _ in range(n)]
result[0][0] = 1

# up, down, left, right
xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0]

def bfs(arr, start):
    queue = deque([start])
    while queue:
        pop = queue.popleft()
        y, x = pop[0], pop[1]
        num = result[y][x]
        for i in range(4):
            ny, nx = y+ycor[i], x+xcor[i]
            if ny not in ([-1, n]) and nx not in ([-1, m]):
                if arr[ny][nx] != 0 and visited[ny][nx] == False:
                    result[ny][nx] = num + 1
                    queue.append((ny, nx))
                    visited[ny][nx] = True

def solution(arr):
    bfs(arr, (0, 0))

solution(arr)
print(result[n-1][m-1])
