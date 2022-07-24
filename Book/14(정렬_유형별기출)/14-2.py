# 안테나(백준_18310)

import sys
input = sys.stdin.readline

n = int(input())
housepos = list(map(int, input().split()))

##--------------------------------------------------------------------------##
# 시도1. 시간 초과
# inf = int(1e9)

# def solution(housepos):
#     minanswer = (0, inf)
#     for i in housepos:
#         cnt = 0
#         for j in housepos:
#             cnt += abs(i-j)
#         if cnt < minanswer[1]:
#             minanswer = (i, cnt)
#     answer = minanswer[0]
#     return answer

# print(solution(housepos))
##--------------------------------------------------------------------------##
# 시도2. 중앙값의 성질
def solution(n, housepos):
    housepos.sort()
    answer = housepos[(n//2)-1]
    return answer

print(solution(n, housepos))

