# 절댓값 힙

import sys; input = sys.stdin.readline
import heapq

n = int(input())

xlist = []
for _ in range(n):
    x = int(input())
    if x != 0:
        if x < 0:
            heapq.heappush(xlist, (-(x), -1))
        else:
            heapq.heappush(xlist, (x, 1))
    else:
        if len(xlist) == 0:
            print(0)
        else:
            result = heapq.heappop(xlist)
            print(result[0]*result[1])

