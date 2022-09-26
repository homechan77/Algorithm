# 팩토리얼 0의 개수

import sys

input = sys.stdin.readline

n = int(input())

def solution(n):
    answer = 0
    while n > 0:
        answer += (n//5)
        n = n//5
    return answer

print(solution(n))