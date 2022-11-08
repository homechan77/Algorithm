# 테트로미노
# 참고) https://cijbest.tistory.com/87

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

result = 0

# 상 하 좌 우
xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0]

# "ㅜ"를 제외한 나머지가 상하좌우 4칸 이동 조합의 모든 경우의 수이다.
def dfs(y, x, score, cnt):
    global result

    if cnt == 4:
        if score > result:
            result = score
        return
    
    for i in range(4):
        newy, newx = y+ycor[i], x+xcor[i]
        if newy not in ([-1, n]) and newx not in ([-1, m]) and visited[newy][newx]==False:
            visited[newy][newx] = True
            dfs(newy, newx, score+arr[newy][newx], cnt+1)
            visited[newy][newx] = False

def remains(y, x):
    global result

    for i in range(4):
        tmp = arr[y][x]
        for j in range(3):
            k = (i+j)%4
            newy, newx = y+ycor[k], x+xcor[k]
            if not (newy not in ([-1, n]) and newx not in ([-1, m])):
                tmp = 0
                break
            tmp += arr[newy][newx]
        if tmp > result:
            result = tmp     

def solution(n, m):
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, arr[i][j], 1)
            visited[i][j] = False
            remains(i, j)

solution(n, m)
print(result)
