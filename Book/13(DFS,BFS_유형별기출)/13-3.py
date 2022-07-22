# 경쟁적 전염(백준_18405)
# "이미 방문한 위치는 방문할 필요가 없다."

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

##--------------------------------------------------------------------------##
# 시간 초과
# def virusspread(a, presentcor):
#     # 상하좌우
#     xcor = [0, 0, -1, 1]
#     ycor = [-1, 1, 0, 0]
    
#     tmp = []
#     for i in range(n):
#         for j in range(n):
#             if (lab[i][j] == a) and ([i,j] in (presentcor)):
#                 for k in range(4):
#                     x = j+xcor[k]
#                     y = i+ycor[k]
#                     if not (x in ([-1, n]) or y in ([-1, n])):
#                          if lab[y][x] == 0:
#                              lab[y][x] = a
#                              tmp.append([y,x])
#     presentcor.extend(tmp)
#     return presentcor
##--------------------------------------------------------------------------##

def virusspread(a, presentcor):
    # 상하좌우
    xcor = [0, 0, -1, 1]
    ycor = [-1, 1, 0, 0]
    
    tmp = []
    queue = deque(presentcor)
    while queue:
        pop = queue.popleft()
        for i in range(4):
            x = pop[1]+xcor[i]
            y = pop[0]+ycor[i]
            
            if not (x in ([-1, n]) or y in ([-1, n])):
                if lab[y][x] == 0:
                    lab[y][x] = a
                    tmp.append([y,x])
    return tmp
        
    
def solution(k, s, lab, x, y):
    presentcor = [[] for _ in range(k+1)]
    for i in range(n):
        for j in range(n):
            if 1 <= lab[i][j] <= k:
                presentcor[lab[i][j]].append([i,j])
    
    for _ in range(s):
        for kr in range(k):
            presentcor[kr+1] = virusspread(kr+1, presentcor[kr+1])

    answer = lab[x-1][y-1]
    return answer

print(solution(k, s, lab, x, y))