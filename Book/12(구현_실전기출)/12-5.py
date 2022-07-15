# 뱀

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
k = int(input())
klist = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
llist = [list(input().split()) for _ in range(l)]

board = [[0]*n for _ in range(n)]
for i in klist:
    board[i[0]-1][i[1]-1] = 999
board[0][0] = 1
        
direction = 'right'
cnt = 0
x, y = 0, 0
snake = deque([(0, 0)])

def moving():
    global board, direction, cnt, x, y, snake
    
    alarm = False
    cnt += 1
    if direction == 'right':
        x += 1
        if x >= n:
            alarm =True
            return alarm
    elif direction == 'left':
        x -= 1
        if x < 0:
            alarm =True
            return alarm
    elif direction == 'up':
        y -= 1
        if y < 0:
            alarm =True
            return alarm
    else:
        y += 1
        if y >= n:
            alarm =True
            return alarm
            
    if board[y][x] == 999:
        board[y][x] = 1
        snake.append((y, x))
    else:
        board[y][x] += 1
        snake.append((y, x))
        if board[y][x] > 1:
            alarm =True
            return alarm
        pop = snake.popleft()
        board[pop[0]][pop[1]] = 0
    
    return alarm, board, direction, cnt, x, y, snake

def changedirection(a):
    global direction
    
    if a == 'D':
        if direction == 'right':
            direction = 'down'
        elif direction == 'left':
            direction = 'up'
        elif direction == 'up':
            direction = 'right'
        elif direction == 'down':
            direction = 'left'
    else:
        if direction == 'right':
            direction = 'up'
        elif direction == 'left':
            direction = 'down'
        elif direction == 'up':
            direction = 'left'
        elif direction == 'down':
            direction = 'right'
    

def solution(n, klist, llist):
    global board, direction, cnt, x, y, snake
    for i in llist:
        while cnt < int(i[0]):
            alarm = moving()
            if alarm is True:
                return cnt
        changedirection(i[1])
    
    while True:
        alarm = moving()
        if alarm is True:
            return cnt

print(solution(n,klist, llist))