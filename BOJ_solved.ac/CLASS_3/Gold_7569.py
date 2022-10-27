# 토마토

import sys; input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split()) # 가로, 세로, 높이

box = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    box.append(tmp)

visited = [[[False]*M for _ in range(N)] for _ in range(H)]

# up, down, left, right
xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0]
# front, back
hcor = [1, -1]

def bfs(onecor):
    queue = deque(onecor)
    while queue:
        h, r, c, day = queue.popleft()
        for i in range(4):
            new_r, new_c = r+ycor[i], c+xcor[i]
            if new_r not in [-1, N] and new_c not in [-1, M]:
                if box[h][new_r][new_c] not in [1, -1]:
                    queue.append((h, new_r, new_c, day+1))
                    box[h][new_r][new_c] = 1
                    visited[h][new_r][new_c] = True
        for j in range(2):
            new_h = h+hcor[j]
            if new_h not in [-1, H]:
                if box[new_h][r][c] not in [1, -1]:
                    queue.append((new_h, r, c, day+1))
                    box[new_h][r][c] = 1
                    visited[new_h][r][c] = True
        
        if len(queue) == 0:
            return day

def solution(N, M, H):
    onecor = []
    cnt = 0
    for i in range(H):
        for r in range(N):
            for c in range(M):
                if box[i][r][c] == 1:
                    onecor.append((i, r, c, 0))
                    visited[i][r][c] = True
                    cnt += 1
                elif box[i][r][c] == -1:
                    visited[i][r][c] = True
                    cnt += 1
    if cnt == N*M*H:
        return 0
    else:
        day = bfs(onecor)
    
    for i in range(H):
        for r in range(N):
            for c in range(M):
                if visited[i][r][c] == False:
                    return -1
    return day

print(solution(N, M, H))