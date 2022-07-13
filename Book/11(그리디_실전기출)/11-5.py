# 볼링공 고르기

# 나의 코드_조합 라이브러리 활용
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

def solution(nlist):
    clist = combinations(nlist, 2)
    answer = 0
    for i in clist:
        if i[0] != i[1]:
            answer+=1
    return answer

print(solution(nlist))
##--------------------------------------------------------------------------##
# 답안 코드_그리디 알고리즘 활용
import sys

n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

def solution2(n, m, nlist):
    array = [0]*11
    for i in nlist:
        array[i] += 1
    answer = 0
    for j in range(1, m+1):
        n -= array[j]
        answer += array[i]*n
    return answer

print(solution2(n,m,nlist))