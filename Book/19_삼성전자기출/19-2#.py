# 청소년 상어(백준_19236)

import sys
import copy

input = sys.stdin.readline
fishinfo = [list(map(int, input().split())) for _ in range(4)]

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
xcor = [0, -1, -1, -1, 0, 1, 1, 1]
ycor = [-1, -1, 0, 1, 1, 1, 0, -1]

result = 0

# dfs 활용, 상어가 갈 수 있는 모든 좌표 완전 탐색을 통하여 최대값 도출
def dfs(graph, shark_now, eatfish):
    global result

    graph = copy.deepcopy(graph)

    eatfish += graph[shark_now[0]][shark_now[1]][0]
    
    graph = fish_move(graph, shark_now)
    
    pos_po = shark_move(graph, shark_now)
    
    graph[shark_now[0]][shark_now[1]] = [0, 0]
     
    if len(pos_po) > 0:
        for i in pos_po:
            dfs(graph, i, eatfish)
    else:
        if eatfish > result:
            result = eatfish


# 상어가 갈 수 있는 좌표값 추출 
def shark_move(graph, shark_now):
    direc = graph[shark_now[0]][shark_now[1]][1]
    possible_position = []
    while True:
        x = shark_now[1]+xcor[direc-1]
        y = shark_now[0]+ycor[direc-1]
        if x in ([-1, 4]) or y in ([-1, 4]):
            break
        if graph[y][x] != [0, 0]:
            possible_position.append([y, x])
        shark_now = [y, x]
    return possible_position


# 물고기 움직임(1)_수정 성공
def fish_move(graph, shark_now):
    graph[shark_now[0]][shark_now[1]][0] = 99

    position = [[] for _ in range(17)]
    for i in range(4):
        for j in range(4):
            if graph[i][j] == [0, 0] or graph[i][j][0] == 99:
                continue
            position[graph[i][j][0]].extend([i, j])

    for n, i in enumerate(position):
        if len(i) == 0 or n == 0:
            continue
        target = graph[i[0]][i[1]]
        tar_d = target[1]
        my, mx = i[0]+ycor[tar_d-1], i[1]+xcor[tar_d-1]
        if  mx not in ([-1, 4]) and my not in ([-1, 4]) and graph[my][mx][0] != 99:
            position[graph[my][mx][0]] = i
            graph[i[0]][i[1]] = graph[my][mx]
            graph[my][mx] = target
        else:
            for k in range(1, 8):
                new_direct = ((tar_d-1)+k) % 8
                my, mx = i[0]+ycor[new_direct], i[1]+xcor[new_direct]
                if mx not in ([-1, 4]) and my not in ([-1, 4]) and graph[my][mx][0] != 99:
                    position[graph[my][mx][0]] = i
                    graph[i[0]][i[1]] = graph[my][mx]
                    graph[my][mx] = [target[0], new_direct+1]
                    break
    return graph

# 물고기 움직임(2)_책 참조
# def find_fish(graph, num):
#     for i in range(4):
#         for j in range(4):
#             if graph[i][j][0] == num:
#                 return (i, j)
#     return None

# def fish_move(graph, shark_now):
#     graph[shark_now[0]][shark_now[1]][0] = 99

#     for i in range(1, 17):
#         position = find_fish(graph, i)
#         if position != None:
#             y, x = position[0], position[1]
#             tar_d = graph[y][x][1]
#             for k in range(8):
#                 new_direct = ((tar_d-1)+k) % 8
#                 my, mx = y+ycor[new_direct], x+xcor[new_direct]
#                 if mx not in ([-1, 4]) and my not in ([-1, 4]):
#                     if graph[my][mx][0] != 99:
#                         graph[y][x][1] = new_direct+1
#                         graph[y][x], graph[my][mx] = graph[my][mx], graph[y][x]
#                         break
#     return graph


def solution(fishinfo):
    graph = [[] for _ in range(4)]
    for i in range(4):
        for j in range(len(fishinfo[0])):
            if j%2 == 0:
                graph[i].append([fishinfo[i][j], fishinfo[i][j+1]])
    
    start = [0, 0]
    dfs(graph, start, 0)

    return result

print(solution(fishinfo))