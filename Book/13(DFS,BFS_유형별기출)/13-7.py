# 인구 이동(백준_16234)

##--------------------------------------------------------------------------##
# # 시도1. 반례 미통과
# # 4 1 9
# # 96 93 74 30
# # 60 90 65 96
# # 5 27 17 98
# # 10 41 46 20
# # 답: 1

# import sys
# from collections import deque

# input = sys.stdin.readline
# n, l, r = list(map(int, input().split()))
# nationboard = [list(map(int, input().split())) for _ in range(n)]
# isblock = [[False for _ in range(n)] for _ in range(n)]

# xcor = [0, 0, -1, +1]
# ycor = [-1, +1, 0, 0]

# def newnationboard(board, qblock):
#     result = []
#     for i in range(n):
#         for j in range(n):
#             if qblock[i][j] == True:
#                 tmp = []
#                 queue = deque([[i, j]])
#                 while queue:
#                     pop = queue.popleft()
#                     for d in range(4):
#                         x, y = pop[1]+xcor[d], pop[0]+ycor[d]
#                         if (x in ([-1, n]) or y in ([-1, n])) or [y, x] in (list(queue)):
#                             continue
#                         if qblock[y][x] == True:
#                             queue.append([y, x])
#                     tmp.append(pop)
#                     qblock[pop[0]][pop[1]] = False
#                 result.append(tmp)
#     for r in result:
#         rn = len(r)
#         suml = sum(map(lambda x: board[x[0]][x[1]], r))
#         newn = suml // rn
#         for i in r:
#             board[i[0]][i[1]] = newn
    
#     return board, qblock
    
                                
# def blockcheck(board, y, x):
#     global n, l, r
    
#     for i in range(4):
#         xd = x+xcor[i]
#         yd = y+ycor[i]
#         if (xd in ([-1, n]) or yd in ([-1, n])):
#             continue
#         if l <= abs(board[y][x] - board[yd][xd]) <= r:
#             return True
#         else:
#             continue
    
#     return False

# def solution(n, nationboard, isblock):
#     answer = 0
#     while True:
#         cnt = 0
#         for i in range(n):
#             for j in range(n):
#                 a = blockcheck(nationboard, i, j)
#                 isblock[i][j] = a
#                 if a is False:
#                     cnt += 1
#         if cnt == (n*n):
#             return answer
#         nationboard, isblock = newnationboard(nationboard, isblock)
#         answer += 1

# print(solution(n, nationboard, isblock))

##--------------------------------------------------------------------------##
# 시도2. 성공_dfs 활용

import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n, l, r = list(map(int, input().split()))
nationboard = [list(map(int, input().split())) for _ in range(n)]

xcor = [0, 0, -1, +1]
ycor = [-1, +1, 0, 0]

def newnationboard(listr):
    for i in listr:
        newn = sum(map(lambda x: nationboard[x[0]][x[1]], i)) // len(i)
        for j in i:
            nationboard[j[0]][j[1]] = newn

def check(y, x, visited, result):
    global n, l, r
    
    alarm = False
    for d in range(4):
        xd, yd = x+xcor[d], y+ycor[d]
        if xd in ([-1, n]) or yd in ([-1, n]):
            continue
        if (l <= abs(nationboard[y][x]-nationboard[yd][xd]) <= r) and (visited[yd][xd] is False): 
            if not alarm:
                result.append([y, x])
                visited[y][x] = True
                alarm = True
            check(yd, xd, visited, result)
    if not alarm:
        result.append([y, x])
        visited[y][x] = True
    
    return result, visited
        
def solution(n):
    answer = 0
    while True:
        visited = [[False for _ in range(n)] for _ in range(n)]
        result = []
        for i in range(n):
            for j in range(n):
                if visited[i][j] == True:
                    continue
                tmp = []
                tmp, visited = check(i, j, visited, tmp)
                if len(tmp) > 1:
                    result.append(tmp)
        if len(result) <= 0:
            return answer
        newnationboard(result)
        answer += 1

print(solution(n))