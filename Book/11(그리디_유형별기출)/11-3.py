# 문자열 뒤집기(백준_1439)
import sys
s = list(sys.stdin.readline().strip())
def solution(s):
    cnt1 = 0
    cnt0 = 0
    alarm1 = False
    alarm0 = False
    for i in s:
        if i=='0' and alarm1 is True:
            cnt1 += 1
            alarm1 = False
            alarm0 = True
            continue
        if i=='1' and alarm0 is True:
            cnt0 += 1
            alarm0 = False
            alarm1 = True
            continue
        if i == '0':
            alarm0 = True
        else:
            alarm1 = True
    if s[-1] == '0':
        cnt0+=1
    else:
        cnt1+=1
    answer = min(cnt0, cnt1)
    return answer

print(solution(s))