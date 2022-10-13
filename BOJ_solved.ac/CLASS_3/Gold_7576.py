# 토마토
# recommit

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# up, down, left, right
xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0]

def bfs(m, n, arr):
    queue = deque([])
    notify = False
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                queue.append([(r,c), 0])
            elif arr[r][c] == 0:
                notify = True
    
    # 상황1. 모두 1인 경우(토마토가 모두 익어 있는 상태)
    if not notify:
        return 0, notify
    # 상황2. 모두 0인 경우(토마토가 모두 익지 못하는 상태_익어 있는 토마토가 없다)
    if len(queue) == 0:
        return -1, notify
    
    while queue:
        pop = queue.popleft()
        row , col = pop[0]
        cnt = pop[1]
        for i in range(4):
            nrow, ncol = row+ycor[i], col+xcor[i]
            if nrow not in (-1, n) and ncol not in (-1, m):
                if arr[nrow][ncol] == 0:
                    arr[nrow][ncol] = 1
                    queue.append([(nrow, ncol), cnt+1])
        if len(queue) == 0:
            return cnt, arr

def solution(m, n, arr):
    result, afterarr = bfs(m, n, arr)
    # 상황 1에 대한 출력
    if afterarr == False:
        return result
    # 상황 2에 대한 출력
    elif afterarr == True:
        return result
    # 그 외 정상적인 상황이라면 cnt와 arr을 반환
    else:
        for r in range(n):
            for c in range(m):
                if afterarr[r][c] == 0:
                    return -1
    return result

print(solution(m, n, arr))