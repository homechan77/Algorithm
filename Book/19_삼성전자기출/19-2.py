# 청소년 상어(백준_19236)

import sys

input = sys.stdin.readline
fishinfo = [list(map(int, input().split())) for _ in range(4)]

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
xcor = [0, 0, -1, -1, -1, 0, 1, 1, 1]
ycor = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# def dfs()

def solution(fishinfo):
    fish = []
    for i in range(4):
        tmp = []
        for j in range(len(fishinfo[i])-1):
            if j % 2 == 0:
                tmp.append((fishinfo[i][j], fishinfo[i][j+1]))
        fish.append(tmp)
        
    shark_now = fish[0][0]
    while True:
        for f in range(1, 17):
            for i in range(n):
                for j in range(n):
                    if fish[i][j][0] == f:
                        y = i + ycor[fish[i][j][1]]
                        x = j + xcor[fish[i][j][1]]
                        if x in ([-1, 4]) or y in ([-1, 4]) or fish[y][x] == shark_now:
                            if f not in fish:
                                

    return fish

print(solution(fishinfo))