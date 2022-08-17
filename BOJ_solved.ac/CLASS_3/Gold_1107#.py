# 리모컨

import sys

input = sys.stdin.readline

n = int(input())
m = int(input()) # 고장난 숫자 버튼의 개수
if m != 0:
    mlist = list(map(int, input().split())) # 고장난 숫자 버튼들
    if m != 10:
        possible_button = [i for i in range(10) if i not in (mlist)]
    else:
        possible_button = [-1] # 모든 숫자 버튼이 고장난 경우
else:
    possible_button = [i for i in range(10)] # 고장난 숫자의 버튼이 없는 경우 = 모든 버튼의 숫자 사용 가능

def check(target):
    starget = str(target)
    cnt = 0
    for i in starget:
        if int(i) not in (possible_button):
            return False
    return True

def solution(n):
    result = 0
    minus, plus = n, n
    diff = abs(n-100)
    if diff == 0:
        return diff
    noti_m = False
    while diff > result+len(str(minus)):
        if not noti_m:
            if check(minus):
                return result+len(str(minus))
            minus -= 1
            if minus < 0:
                noti_m = True
        if check(plus):
            return result+len(str(plus))
        plus += 1
        result += 1
    return diff

print(solution(n))
