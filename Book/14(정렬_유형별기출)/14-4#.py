# 카드 정렬하기(백준_1715)

import sys
import heapq
input = sys.stdin.readline

n = int(input())
cardlist = [int(input()) for _ in range(n)]

def solution(cardlist):
    heapq.heapify(cardlist)
    result = 0
    while len(cardlist) != 1:
        a = heapq.heappop(cardlist)
        b = heapq.heappop(cardlist)
        tmp = a+b
        result += tmp
        heapq.heappush(cardlist, tmp)
    
    return result

print(solution(cardlist))