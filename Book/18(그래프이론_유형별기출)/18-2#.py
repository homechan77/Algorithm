# 탑승구

import sys

input = sys.stdin.readline
g = int(input())
p = int(input())
gi = [int(input()) for _ in range(p)]

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

def solution(g, p):
    parent = [0 for _ in range(g+1)]
    for i in range(g+1):
        parent[i] = i
    answer = 0
    for i in range(p):
        data = find_parent(parent, gi[i])
        if data == 0:
            break
        union_parent(parent, data, data-1)
        answer += 1
    return answer

print(solution(g, p))