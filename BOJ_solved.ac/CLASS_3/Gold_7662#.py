# 이중 우선순위 큐

'''
# 시도1. 실패

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    heap = []
    for _ in range(int(input())):
        string, integer = input().split()
        integer = int(integer)
        if string == 'I':
            heappush(heap, integer)
        else:
            if len(heap) == 0:
                continue
            if integer == -1:
                heappop(heap)
            else:
                heap.pop()
    if len(heap) == 0:
        print("EMPTY")
    else:
        print(heap[-1], heap[0], sep=' ')
'''

##--------------------------------------------------------------------------##
'''
# 시도2. 시간초과_이진탐색 삽입 활용 
import sys
sys.setrecursionlimit(10**6)
from collections import deque

input = sys.stdin.readline

t = int(input())

def binarysearch(arr, target, start, end):
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarysearch(arr, target, mid+1, end)
    else:
        return binarysearch(arr, target, start, mid-1)

def solution(t):
    for _ in range(t):
        arr = deque([])
        for _ in range(int(input())):
            Str , Num = input().split()
            Num = int(Num)
            if Str == 'I':
                if len(arr) == 0:
                    arr.append(Num)
                else:
                    result = binarysearch(arr, Num, 0, len(arr)-1)
                    arr.insert(result, Num)
            else:
                if len(arr) == 0:
                    continue
                if Num == 1:
                    arr.pop()
                elif Num == -1:
                    arr.popleft()

        if len(arr) == 0:
            print("EMPTY")
        else:
            print(arr[-1], arr[0], sep=' ')

solution(t)
'''

##--------------------------------------------------------------------------##
# 시도3. 정답자 코드 참조
import sys
import heapq

input = sys.stdin.readline

t = int(input())

def solution(t):
    for _ in range(t):
        minH, maxH = [], []
        visited = [False] * 1000000
        for i in range(int(input())):
            Str, Num = input().split()
            Num = int(Num)
            if Str == 'I':
                heapq.heappush(minH, (Num, i))
                heapq.heappush(maxH, (-(Num), i))
                visited[i] = True
            else:
                if Num == -1:
                    while minH and not visited[minH[0][1]]:
                        heapq.heappop(minH)
                    if minH:
                        visited[minH[0][1]] = False
                        heapq.heappop(minH)
                elif Num == 1:
                    while maxH and not visited[maxH[0][1]]:
                        heapq.heappop(maxH)
                    if maxH:
                        visited[maxH[0][1]] = False
                        heapq.heappop(maxH)
        
        while minH and not visited[minH[0][1]]: heapq.heappop(minH)
        while maxH and not visited[maxH[0][1]]: heapq.heappop(maxH)

        if minH and maxH:
            print(-(maxH[0][0]), minH[0][0], end=' ')
        else:
            print("EMPTY")

solution(t)

