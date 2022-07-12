# 모험가 길드
import sys
n = int(sys.stdin.readline())
nlist = sorted(list(map(int, sys.stdin.readline().split())))

def solution(n, nlist):
    answer = 0
    cnt = 0
    for i in range(n):
        cnt += 1
        if cnt >= nlist[i]:
            answer += 1
            cnt = 0
    return answer

print(solution(n, nlist))
