# 곱하기 혹은 나누기
import sys

s = list(sys.stdin.readline().strip())

def solution(s):
    answer = 0
    for i in s:
        if answer<=1 or int(i)<=1:
            answer += int(i)
        else:
            answer *= int(i)
    return answer

print(solution(s))