# 여행 계획

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
travelplan = list(map(int, input().split()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    xa = find_parent(parent, x)
    yb = find_parent(parent, y)
    if xa > yb:
        parent[xa] = yb
    else:
        parent[yb] = xa
    return parent

def solution(n, m, graph, travelplan):
    parent = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        parent[i] = i
    information = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                information.append((i+1, j+1))
    for i in information:
        a, b = i[0], i[1]
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        parent = union_parent(parent, a, b)            
    
    result = True
    for t in range(m-1):
        if find_parent(parent, travelplan[t]) != find_parent(parent, travelplan[t+1]):
            result = False
    if result:
        print('YES')
    else:
        print('NO')
    # result = []
    # for i in travelplan:
    #     result.append(parent[i])
    # if len(set(result)) == 1:
    #     print('YES')
    # else:
    #     print('NO')

solution(n, m, graph, travelplan)