# 1로 만들기

# 시도1. 시간초과
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

def bfs(n):
    queue = deque([[n, 0]])
    while True:
        pop = queue.popleft()
        i, cnt = pop[0], pop[1]
        if i == 1:
            return cnt
        if i % 3 == 0:
            queue.append([i//3, cnt+1])
        if i % 2 == 0:
            queue.append([i//2, cnt+1])
        queue.append([i-1, cnt+1])   

def solution(n):
    answer = bfs(n)
    return answer

print(solution(n))

