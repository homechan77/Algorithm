# # import sys
# # from collections import deque

# # 시도1. 실패
# # def solution(plantlive):
# #     queue = deque(plantlive)
# #     tmp = []
# #     while queue:
# #         pop = queue.popleft()
# #         if len(tmp) == 0:
# #             tmp.append([pop])
# #             continue
# #         popup, popdown, popleft, popright = [pop[0], pop[1]+1], [pop[0], pop[1]-1], [pop[0]-1, pop[1]], [pop[0]+1, pop[1]]
# #         alarm = False
# #         for i in tmp:
# #             for j in i:
# #                 if j in [popup, popdown, popleft, popright]:
# #                     i.append(pop)
# #                     alarm = True
# #                     break
# #         if alarm is False:
# #             tmp.append([pop])
# #     return len(tmp)
          
# # t = int(sys.stdin.readline())
# # answerlist =[]
# # for _ in range(t):
# #     n, m, k = map(int, sys.stdin.readline().split())
# #     plantlive = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(k)],
# #                        key=lambda x: (-x[0],x[1]))
# #     answer = solution(plantlive)
# #     answerlist.append(answer)

# # for i in answerlist:
# #     print(i)
# ##--------------------------------------------------------------------------##
# # 시도2. dfs_실패
# import sys
# from collections import deque

# def solution2(plantmap, visited):
#     queue = deque(plantmap)
#     while queue:
#         pop = queue.popleft()
#         visited[pop[1]] = True
#         popup, popdown, popleft, popright = [pop[1][0], pop[1][1]+1], 
#                                             [pop[1][0], pop[1][1]-1], 
#                                             [pop[1][0]-1, pop[1][1]], 
#                                             [pop[1][0]+1, pop[1][1]]
#         for i in queue:
#             if i[1] in [popup, popdown, popleft, popright]:
#                 if not visitedp[i[0]]:
#                     solution2(plantmap, visited)
        
# ##--------------------------------------------------------------------------##
# 시도3. 정답자 코드 참조_dfs
import sys
sys.setrecursionlimit(10000) # 기본 재귀 한도: 1000 / 이를 넘어갈 경우 추가로 모듈 선언

def dfs(x, y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<m) and (0<=ny<n):
            if matrix[ny][nx] == 1:
                matrix[ny][nx] = -1
                dfs(nx, ny)

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0]*m for _ in range(n)]
    cnt = 0
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                dfs(j, i)
                cnt += 1
    print(cnt)
    
##--------------------------------------------------------------------------##
# 시도4. 정답자 코드 참조_bfs
import sys
from collections import deque

def bfs(x, y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<m) and (0<=ny<n) and matrix[ny][nx] == 1:
                queue.append((nx, ny))
                matrix[ny][nx] = 2
    return 1
            

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0]*m for _ in range(n)]
    cnt = 0
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                cnt += bfs(j, i)
    
    print(cnt)