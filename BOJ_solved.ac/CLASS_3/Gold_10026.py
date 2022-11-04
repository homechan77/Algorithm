# 적록색약

import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
img = [input().rstrip() for _ in range(n)]

# up, down, left, right
xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0] 

def bfs(inputr, inputc, inputcolor, flag, visited):
    global n

    queue = deque([(inputr, inputc, inputcolor)])
    while queue:
        r, c, color = queue.popleft()
        for i in range(4):
            new_r, new_c = r+ycor[i], c+xcor[i]
            if (new_r not in [-1, n] and new_c not in [-1, len(img[0])]) and (visited[new_r][new_c] == False):
                if flag == False:
                    if img[new_r][new_c] == color:
                        visited[new_r][new_c] = True
                        queue.append((new_r, new_c, color))
                else:
                    if color in ['R', 'G']:
                        if img[new_r][new_c] in ['R', 'G']:
                            visited[new_r][new_c] = True
                            queue.append((new_r, new_c, color))
                    else:
                        if img[new_r][new_c] == color:
                            visited[new_r][new_c] = True
                            queue.append((new_r, new_c, color))
    return visited

flag = False
for f in range(2):
    if f == 1:
        flag = True
    visited = [[False]*len(img[0]) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(len(img[0])):
            if visited[i][j] == False:
                result += 1
                visited[i][j] = True
                visited = bfs(i, j, img[i][j], flag, visited)
    print(result, end=' ')

