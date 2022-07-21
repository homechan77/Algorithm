# 감시 피하기(백준_18428)

import sys
from itertools import combinations
import copy

input = sys.stdin.readline
n = int(input())
board = [list(input().split()) for _ in range(n)]

def detect(board, d, y, x):
    global n
    xcor = [0, 0, -1, 1]
    ycor = [-1, 1, 0, 0]
    xp = x+xcor[d]
    yp = y+ycor[d]
    if (xp in ([-1, n]) or yp in ([-1, n])) or (board[yp][xp] == 'O'):
        return True
    elif board[yp][xp] == 'S':
        return False
    elif board[yp][xp] in (['X', 'T']):
        return detect(board, d, yp, xp)
    
    
def check(board, teachercor):
    for i in teachercor:
        for d in range(4):
            if not detect(board, d, i[0], i[1]):
                return False
    return True
                                        
    
def solution(n, board):
    blankcor = []
    teachercor = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                blankcor.append([i, j])
            elif board[i][j] == 'T':
                teachercor.append([i, j])
    blankcor_combi = list(combinations(blankcor, 3))
    
    for bc in blankcor_combi:
        boardcopy = copy.deepcopy(board)
        for i in bc:
            boardcopy[i[0]][i[1]] = 'O'
        if check(boardcopy, teachercor):
            print('YES')
            return
    print('NO')
    return
            
solution(n, board)