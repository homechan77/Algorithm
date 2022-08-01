# 병사 배치하기(백준_18353)
# 가장 긴 증가하는 부분수열(LIS) 알고리즘 활용

import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

def solution(n, array):
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if array[j] > array[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return n-max(dp)


print(solution(n, array))