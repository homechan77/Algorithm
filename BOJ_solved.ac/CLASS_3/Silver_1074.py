# Z
import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

graph = [[0]*(2**n) for _ in range(2**n)]

cnt = 1
def dfs(n, start):
    global cnt

    point = detection(start):
    for i in range(point)


    if n != cnt:
        dfs(n-1)
    else:
        
xcor = [0, 1, 0, 1]
ycor = [0, 0, 1, 1]

def detection(cor):
    point = []
    y, x = cor
    for i in range(4):
        ym, xm = y+ycor[i], x+xcor[i]
        point.append((ym, xm))
    return point

def solution():
    dfs(n, (0, 0))