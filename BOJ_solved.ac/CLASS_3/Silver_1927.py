# 최소 힙

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

def solution(n):
    heap = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            if len(heap) == 0:
                print(0)
            else:
                pop = heappop(heap)
                print(pop)
        else:
            heappush(heap, x)

solution(n)
