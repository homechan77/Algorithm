# 어른 상어(백준_19237)

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split()) # 격자 크기, 상어 수, 냄새 사라지기 위한 시간
graph = [list(map(int, input().split())) for _ in range(n)] # 격자의 모습(초기 상어 위치)
shark_direct = list(map(int, input().split())) # 초기 상어 방향: 상하좌우(1,2,3,4)
shark_priority = [[] for _ in range(m)] # 각 상어들의 방향에 따른 이동 우선순위
for i in range(m*4):
    tmpinput = list(map(int, input().split()))
    shark_priority[i // 4].append(tmpinput)

xcor = [0, 0, 0, -1, 1]
ycor = [0, -1, 1, 0, 0]

smell_graph = [[[0, 0] for _ in range(n)] for _ in range(n)]
def put_smell():
    for i, c in enumerate(shark_position):
        if c == [-1, -1]:
            continue
        y, x = c[0], c[1]
        smell_graph[y][x] = [i+1, k]

def discount_smell():
    for i in range(n):
        for j in range(n):
            if smell_graph[i][j][1] != 0:
                smell_graph[i][j][1] -= 1
                if smell_graph[i][j][1] == 0:
                    smell_graph[i][j] = [0, 0]

shark_position = [[] for _ in range(m)]
def shark_find():
    s_cnt = 1
    while s_cnt <= m:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == s_cnt:
                    shark_position[s_cnt-1].extend([i, j])
                    s_cnt += 1

def shark_move():
    for i in range(1, m+1):
        if shark_position[i-1] == [-1, -1]:
            continue
        now_direct = shark_direct[i-1]
        priority = shark_priority[i-1][now_direct-1]
        y, x = shark_position[i-1][0], shark_position[i-1][1]
        alarm = False
        ifnotlist = []
        for j in priority:
            ym, xm = y+ycor[j], x+xcor[j]
            if ym not in ([-1, n]) and xm not in ([-1, n]):
                if smell_graph[ym][xm][1] == 0:
                    shark_position[i-1] = [ym, xm]
                    shark_direct[i-1] = j
                    alarm = True
                    break
                if smell_graph[ym][xm][0] == i:
                    ifnotlist.append((ym, xm, j))
        if not alarm:
            ym, xm, j = ifnotlist[0]
            shark_position[i-1] = [ym, xm]
            shark_direct[i-1] = j

def shark_fight():
    for i in range(m):
        for j in range(i+1, m):
            if shark_position[i] == shark_position[j]:
                shark_position[j] = [-1, -1]

def solution():
    cnt = 0
    while cnt < 1001:
        if cnt == 0:
            shark_find()
            put_smell()
            cnt+=1
            continue
        shark_move()
        cnt += 1
        shark_fight()
        sharkn = 0
        for i in shark_position:
            if i != [-1, -1]:
                sharkn += 1
        if sharkn == 1:
            return cnt-1
        discount_smell()
        put_smell()
    return -1

print(solution())
