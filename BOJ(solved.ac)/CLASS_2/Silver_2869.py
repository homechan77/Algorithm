import sys

a, b, v = map(int, sys.stdin.readline().split())

# 시도1. 시간 초과
def solution(a, b, v):
    cnt = 0
    day = 0
    while True:
        day += 1
        cnt += a
        if cnt == v:
            return day
        cnt -= b

# print(solution(a, b, v))

# 시도2. 정답자 코드 참조_성공.
import math

def solution2(a, b, v):
    day = math.ceil((v-b)/(a-b))
    return day

print(solution2(a,b,v))
