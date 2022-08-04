# 행성 터널(백준_2887)

import sys
# from itertools import combinations
# import heapq

input = sys.stdin.readline
n = int(input())

# 메모리 초과_1
# planetcor = [list(map(int, input().split())) for _ in range(n)]

# 메모리 초과_2
# planetcor = {}
# for i in range(n):
#     planetcor[i] = list(map(int, input().split())) 

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
def solution(n):
    xcor = []
    ycor = []
    zcor = []
    for i in range(n):
        x, y, z = map(int, input().split())
        xcor.append((x, i))
        ycor.append((y, i))
        zcor.append((z, i))
    xcor.sort()
    ycor.sort()
    zcor.sort()
    
    information = []
    for i in range(n-1):
        information.append((xcor[i+1][0]-xcor[i][0], xcor[i][1], xcor[i+1][1]))
        information.append((ycor[i+1][0]-ycor[i][0], ycor[i][1], ycor[i+1][1]))
        information.append((zcor[i+1][0]-zcor[i][0], zcor[i][1], zcor[i+1][1]))
    information.sort()
    
    parent = [0 for _ in range(n+1)]
    for i in range(n+1):
        parent[i] = i
    
    # information에 데이터를 저렇게 넣어도 실제로는 비용이 적은 순으로 정렬 되었기 때문에
    # 0->1로 가는 비용을 3번 계산한다고 하더라도, 한번 계산한것은 if 문에 필터링 된다.
    answer = 0
    for inf in information:
        c, a, b = inf
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c
    
    return answer
    
    """
    # 메모리 초과_1
    information = []
    for i in range(n-1):
        a = planetcor[i]
        for j in range(i+1, n):
            b = planetcor[j]
            xa, ya, za = a[0], a[1], a[2]
            xb, yb, zb = b[0], b[1], b[2]
            information.append((i, j, min(abs(xa-xb), abs(ya-yb), abs(za-zb))))
    information.sort(key = lambda x: x[2])
    
    parent = [0 for _ in range(n+1)]
    for i in range(n+1):
        parent[i] = i
    
    answer = 0
    for i in information:
        x, y, z = i[0], i[1], i[2]
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            answer += z
    """
    
    """
    # 메모리 초과_2(조합, 우선순위 큐 사용)
    information = []
    combikeys = list(combinations(planetcor.keys(), 2))
    for i in combikeys:
        a = i[0]
        b = i[1]
        xa, ya, za = planetcor[a][0], planetcor[a][1], planetcor[a][2]
        xb, yb, zb = planetcor[b][0], planetcor[b][1], planetcor[b][2]
        heapq.heappush(information, (min(abs(xa-xb), abs(ya-yb), abs(za-zb)), a, b))

    parent = [0 for _ in range(n+1)]
    for i in range(n+1):
        parent[i] = i

    answer = 0
    while information:
        i = heapq.heappop(information)
        x, y, z = i[1], i[2], i[0]
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            answer += z
    """
            

print(solution(n))        
    