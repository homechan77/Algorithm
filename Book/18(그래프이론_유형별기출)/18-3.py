# 어두운 길

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
information = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

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

def solution(n, information):
    parent = [0 for _ in range(n+1)]
    for i in range(n+1):
        parent[i] = i
    all = 0
    result = 0
    for i in information:
        x, y, z = i[0], i[1], i[2]
        all += z
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            result += z
    
    answer = all - result
    return answer

print(solution(n, information))
        