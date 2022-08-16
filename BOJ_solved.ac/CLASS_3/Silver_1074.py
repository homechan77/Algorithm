# Z

import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

# graph 배열 이용시 메모리 초과 발생
# graph = [[0]*(2**n) for _ in range(2**n)]

cnt = 0
alarm = False

def dfs(n, start):
    global cnt, r, c, alarm

    xcor = [0, 2**(n-1), 0, 2**(n-1)]
    ycor = [0, 0, 2**(n-1), 2**(n-1)]

    point = detection(start, xcor, ycor)
    for i in point:
        if n != 1:
            if alarm:
                return

            tmpdiff = point[-1][0] - point[0][0]
            if point[0][0]<=r<=(point[-1][0]+(tmpdiff-1)) and point[0][1]<=c<=(point[-1][1]+(tmpdiff-1)):
                dfs(n-1, i)
            else:
                cnt += (tmpdiff**2)*4
                return
        else:
            if point[0][0]<=r<=point[-1][0] and point[0][1]<=c<=point[-1][1]:
                y, x = i
                if y == r and x == c:
                    alarm = True
                    return
                # graph[y][x] = cnt
                cnt += 1
            else:
                cnt += 4
                return
            
def detection(cor, xcor, ycor):
    point = []
    y, x = cor
    for i in range(4):
        ym, xm = y+ycor[i], x+xcor[i]
        point.append((ym, xm))
    return point

def solution(n, r, c):
    dfs(n, (0, 0))
    return cnt

print(solution(n, r, c))
