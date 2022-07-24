# 블록 이동하기(프로그래머스_kakao)

##--------------------------------------------------------------------------##
# # 시도1. 문제도 완전하게 이해하지 못함, dfs 활용_실패...
# result = []

# def check(cor, cnt, tmplist):
#     global n

#     tmplist.append(cor)
    
#     x1, x2 = cor[0][0], cor[1][0]
#     y1, y2 = cor[0][1], cor[1][1]
    
#     if [x2, y2] == [n-1, n-1]:
#         result.append(cnt)
#         return
    
#     # 가로로 늘어서 있는 경우
#     if (y1 == y2) and (x2 - x1 == 1):
#         # board(x1, y1)이 축인 경우
#         # 아래
#         if (y1+1 < n):
#             if (board[y1+1][x1+1] != 1) and (board[y1+1][x1] != 1) and ([[x1, y1], [x1, y1+1]] not in (tmplist)):
#                 cnt += 1
#                 check([[x1, y1], [x1, y1+1]], cnt, tmplist)
#                 cnt -= 1
        
#         # board(x2, y2)이 축인 경우
#         # 아래
#         if (y2+1 < n):
#             if (board[y2+1][x2-1] != 1) and (board[y2+1][x2] != 1) and ([[x2, y2], [x2, y2+1]] not in (tmplist)):
#                 cnt += 1 
#                 check([[x2, y2], [x2, y2+1]], cnt, tmplist)
#                 cnt -= 1

#         # 오른쪽
#         if (x2+1 < n):
#             if (board[y2][x2+1] != 1) and ([[x2, y2], [x2+1, y2]] not in (tmplist)):
#                 cnt += 1
#                 check([[x2, y2], [x2+1, y2]], cnt, tmplist)
#                 cnt -= 1
#         tmplist.pop()
            
    
#     # 세로로 늘어서 있는 경우
#     elif (x1 == x2) and (y2 - y1 == 1):
#         # board(x1, y1)이 축인 경우
#         # 오른쪽
#         if (x1+1 < n):
#             if (board[y1+1][x1+1] != 1) and (board[y1][x1+1] != 1) and ([[x1, y1], [x1+1, y1]] not in (tmplist)):
#                 cnt += 1
#                 check([[x1, y1], [x1+1, y1]], cnt, tmplist)
#                 cnt -= 1
#         # board(x2, y2)이 축인 경우
#         # 오른쪽
#         if (x1+1 < n):
#             if (board[y2-1][x2+1] != 1) and (board[y2][x1+1] != 1) and ([[x2, y2], [x1+1, y2]] not in (tmplist)):
#                 cnt += 1
#                 check([[x2, y2], [x1+1, y2]], cnt, tmplist)
#                 cnt -= 1
#         # 아래
#         if (y2+1 < n):
#             if (board[y2+1][x2] != 1) and ([[x2, y2], [x2, y2+1]] not in (tmplist)):
#                 cnt += 1
#                 check([[x2, y2], [x2, y2+1]], cnt, tmplist)
#                 cnt -= 1
#         tmplist.pop()
        
        
# def solution(board):
#     start = [[0, 0], [1, 0]]
#     check(start, 0, [])
#     answer = min(result)
        
#     return answer


# board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
# n = len(board)
# print(solution(board))

##--------------------------------------------------------------------------##
# 시도2. 책 정답 코드 참조_bfs 활용
from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 이동
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] ==0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 회전
    # 가로로 놓여져 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위, 아래로 회전
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    # 세로로 놓여져 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽, 오른쪽으로 회전
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
            
    return next_pos    
    
    
def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    queue = deque()
    visited = []
    pos = {(1,1), (1,2)}
    queue.append((pos, 0))
    visited.append(pos)
    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost+1))
                visited.append(next_pos)
    # return 0

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
n = len(board)
print(solution(board))
