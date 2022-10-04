# 회의실 배정

import sys

input = sys.stdin.readline

n = int(input())
schedules = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

def solution(schedules):
    endt = schedules[0][1]
    cnt = 1
    for i in range(1, n):
        if schedules[i][0] >= endt:
            cnt += 1
            endt = schedules[i][1]
    return cnt

print(solution(schedules))
