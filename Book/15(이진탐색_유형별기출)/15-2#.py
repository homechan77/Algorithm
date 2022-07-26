# 고정접 찾기

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == mid:
        return mid
    elif mid < array[mid]:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)

def solution(n, a):
    index = binary_search(a, 0, n-1)
    
    if index == None:
        return -1
    else:
        return index
    
print(solution(n, a))