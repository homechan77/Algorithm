# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
n, x = map(int, input().split())
nlist = list(map(int, input().split()))

def count_by_range(nlist, left_value, right_value):
    right_index = bisect_right(nlist, right_value)
    left_index = bisect_left(nlist, left_value)
    return right_index - left_index

def solution(nlist, x):
    count = count_by_range(nlist, x, x)
    if count == 0:
        print(-1)
    else:
        print(count)

solution(nlist, x)