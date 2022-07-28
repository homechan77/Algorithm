# 정수 삼각형(백준_1932)

import sys

input = sys.stdin.readline
n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]

def solution(n, nlist):
    dp = [[] for _ in range(n)]
    dp[0].append(nlist[0][0])
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i].append(dp[i-1][0]+nlist[i][0])
            elif j == i:
                dp[i].append(dp[i-1][j-1]+nlist[i][j])
            else:
                maxn = max(dp[i-1][j-1], dp[i-1][j])
                dp[i].append(maxn+nlist[i][j])
    answer = max(dp[-1])
    return answer
                
print(solution(n, nlist))