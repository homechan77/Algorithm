# 공유기 설치(백준_2110)

##--------------------------------------------------------------------------##
# # 시도1. 이진 탐색_재귀(시간 초과)
# import sys

# n, c = map(int, sys.stdin.readline().split())
# house = sorted([int(sys.stdin.readline()) for _ in range(n)])

# def check(house, distance):
#     global n
    
#     a = 0
#     cnt = 1
#     for i in range(1, n):
#         if house[i]-house[a] >= distance:
#             cnt += 1
#             a = i
#     return cnt
    
# def binary_search(house, start, end):
#     global c
    
#     mid = (start+end) // 2
#     if start > end:
#         return mid
#     if check(house, mid)  < c:
#         return binary_search(house, start, mid-1)
#     else:
#         return binary_search(house, start+1, end)

# def solution(house):
#     mingap = 1
#     maxgap = house[-1] - house[0]
#     answer = binary_search(house, mingap , maxgap)
#     return answer

# print(solution(house))

##--------------------------------------------------------------------------##
# 시도2. 이진 탐색_반복문
import sys

n, c = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(n)])

def binary_search(array, start, end, target):
    global n
    
    while start <= end:
        mid = (start+end) // 2
        standard = 0
        cnt = 1
        for i in range(n):
            if house[i] - house[standard] >= mid:
                cnt += 1
                standard = i
        if cnt < target:
            end = mid-1
        else:
            start = mid+1
    return (start+end)//2
        

def solution(house, c):
    mingap = 1
    maxgap = house[-1] - house[0]
    answer = binary_search(house, mingap, maxgap, c)
    return answer

print(solution(house, c))