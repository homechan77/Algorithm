# 만들 수 없는 금액(백준_저울(2437))

# 내가 작성한 코드_메모리 초과
# import sys
# from itertools import combinations

# n = int(sys.stdin.readline())
# nlist = list(map(int, sys.stdin.readline().split()))

# def solution(n, nlist):
#     clist = []
#     for i in range(1, n+1):
#         clist.extend(list(combinations(nlist, i)))
#     clistsum = list(map(lambda x: sum(x), clist))
#     clistsum = list(set(clistsum))
#     for j in range(1, 1000001):
#         if j not in clistsum:
#             return j
    
# print(solution(n, nlist))
##--------------------------------------------------------------------------##
import sys

n = int(sys.stdin.readline())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
def solution(nlist):
    target = 1
    for i in nlist:
        if target < i:
            break
        target += i
    return target

print(solution(nlist))
