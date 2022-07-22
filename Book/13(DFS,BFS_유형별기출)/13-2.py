# 연구소(백준_14502)

import sys
from itertools import combinations
import copy

input = sys.stdin.readline
n, m = map(int, input().split())
labmap = [list(map(int, input().split())) for _ in range(n)]

def virusspread(map, a, b): # dfs 활용하여 바이러스가 퍼지게 한다.
    global n, m
    # 상,하,좌,우
    ycor = [-1,+1,0,0]
    xcor = [0,0,-1,+1]
    for i in range(4):
        x = a+xcor[i]
        y = b+ycor[i]
        if (x in [-1, m]) or (y in [-1, n]):
            continue
        if map[y][x] in [1, 2]:
            continue
        else:
            map[y][x] = 2
            virusspread(map, x, y)
    return map
            
def solution(n, m, labmap):
    virus = []
    for i in range(n):
        for j in range(m):
            if labmap[i][j] == 0:
                virus.append([i, j])
    wallpos = list(combinations(virus, 3))
    
    labmapcopy = copy.deepcopy(labmap)
    result = []
    for i in wallpos:
        for j in i:
            labmapcopy[j[0]][j[1]] = 1
        for y in range(n):
            for x in range(m):
                if labmapcopy[y][x] == 2:
                    labmapcopy = virusspread(labmapcopy, x, y)
                    
        cnt = 0
        for i in range(n):
            for j in range(m):
                if labmapcopy[i][j] == 0:
                    cnt += 1
        result.append(cnt)
        labmapcopy = copy.deepcopy(labmap)
    
    answer = max(result)
    return answer
    
print(solution(n, m, labmap))