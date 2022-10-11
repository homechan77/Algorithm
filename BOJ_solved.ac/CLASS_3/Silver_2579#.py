# 계단 오르기

'''
# 시도1. 시간 초과(dfs_재귀)
import sys
import copy

input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]

result = 0

def dfs(start, dlist):
    global n, result
    for i in [1, 2]:
        num = start + i
        if num > n:
            continue
        copydlist = copy.deepcopy(dlist)
        if num < n:
            if not ((dlist[-1] == num-1) and (dlist[-2] == num -2)):
                copydlist.append(num)
                dfs(num, copydlist)
        elif num == n:
            if not ((dlist[-1] == num-1) and (dlist[-2] == num -2)):
                copydlist.append(num)
                tresult = sum(map(lambda x: stair[x-1], copydlist[3:]))
                if tresult > result:
                    result = tresult

dfs(0, [-1,-1,-1])
print(result)
'''
##--------------------------------------------------------------------------##
# 시도2. dp

# n개의 계단에서 마지막 n번째 계단으로 올라올 수 있는 경우는 2가지
# case(1) - n-1 계단에서 올라오는 경우, n-2 계단을 지나쳐서는 안된다.(연속된 세 개의 계단을 모두 밟아서는 안 된다)
# -> stairs[n-1] + DP[n-3] + stairs[n]
# case(2) - n-2 계단에서 올라오는 경우, 상관 없다.
# -> DP[n-2] + stairs[n]

import sys

input = sys.stdin.readline

n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

DP = [0]*(n+1)

if n == 1:
    print(stairs[n])
else:
    DP[1] = stairs[1]
    DP[2] = DP[1]+stairs[2]
    for i in range(3, n+1):
        DP[i] = max(stairs[i-1]+DP[i-3]+stairs[i], DP[i-2]+stairs[i])
    # print(DP)
    print(DP[-1])