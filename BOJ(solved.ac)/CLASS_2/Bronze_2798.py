from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

def solution(m, nlist):
    combin = list(combinations(nlist, 3))
    diff = 9999999999
    answer = 0
    for i in range(len(combin)):
        sumi = sum(combin[i])
        if sumi > m:
            continue
        if m-sumi < diff:
            diff = m-sumi
            answer = sumi
    return answer

print(solution(m, nlist))