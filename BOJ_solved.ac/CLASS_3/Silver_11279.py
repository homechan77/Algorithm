# 최대 힙

import sys; input = sys.stdin.readline
import heapq

n = int(input())

def solution(n):
    heap = []
    for _ in range(n):
        x = int(input())
        if x != 0:
            heapq.heappush(heap, -(x))
        else:
            if len(heap) == 0:
                print(0)
            else:
                print(-(heap[0]))
                heapq.heappop(heap)

solution(n)