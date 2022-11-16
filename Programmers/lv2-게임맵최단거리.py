# lv2-게임 맵 최단거리

from collections import deque

xcor = [0, 0, -1, 1]
ycor = [-1, 1, 0, 0]

def bfs(arr, visited, n, m):
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        x = arr[r][c]
        for i in range(4):
            new_r, new_c = r+ycor[i], c+xcor[i]
            if new_r not in ([-1, n]) and new_c not in ([-1, m]) and not visited[new_r][new_c]:
                if 0 < arr[new_r][new_c] <= x:
                    visited[new_r][new_c] = True
                    arr[new_r][new_c] = x+1
                    queue.append((new_r, new_c))
    return arr

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True

    result = bfs(maps, visited, n, m)

    if result[n-1][m-1] == 1:
        return -1
    else:
        return result[n-1][m-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))