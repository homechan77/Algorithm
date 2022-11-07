# 구간 합 구하기 4

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

arr = [0]
for i, a in enumerate(nlist):
    arr.append(arr[-1] + a)

for _ in range(m):
    x, y = map(int, input().split())
    result = arr[y] - arr[x-1]
    print(result)