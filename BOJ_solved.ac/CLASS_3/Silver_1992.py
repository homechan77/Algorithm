# 쿼드트리

import sys

input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]

def dfs(arr, n, rn, cn):
    result = []
    R = arr[rn][cn]
    for r in range(rn, rn+n):
        for c in range(cn, cn+n):
            if arr[r][c] != R:
                if n == 2:
                    return [[arr[rn][cn], arr[rn][cn+1], arr[rn+1][cn], arr[rn+1][cn+1]]]
                splitn = n // 2
                for i, j in [(rn, cn), (rn, cn+splitn), (rn+splitn, cn), (rn+splitn, cn+splitn)]:
                    A = dfs(arr, splitn, i, j)
                    result.extend(A)
                return [result]
    result.append(R)
    return result

def printing(resultarr):
    for j in resultarr:
        if type(j) == list:
            print('(', end='')
            printing(j)
            print(')', end='')
        else:
            print(j, end='')

def solution(n, arr):
    answer = dfs(arr, n, 0, 0)

    if len(answer[0]) == 1:
        print(answer[0])
        return
    
    print('(', end='')
    for i in answer[0]:
        if type(i) == list:
            print('(', end='')
            printing(i)
            print(')', end='')
        else:
            print(i, end='')
    print(')')

solution(n, arr)