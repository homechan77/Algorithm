# 1씩 카운팅 하는 방법
n = int(input())

def solution(n):
    answer = 0
    start = 666
    while True:
        strstart = str(start)
        for i in range(len(strstart)):
            if strstart[i:i+3] == '666':
                answer += 1
                break
            if i+3 == len(strstart):
                break
        if answer == n:
            return start
        start += 1


def solution2(n):
    start = 666
    while n:
        if '666' in str(start):
            n -= 1
        start += 1
    return start-1


print(solution2(n))
    