import sys

n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

# 이분 탐색 활용
def solution(nlist, m):
    start = 1
    end = sum(nlist)
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in nlist:
            if i > mid:
                cnt += (i-mid)
        if cnt < m:
            end = mid-1
        else:
            start = mid+1
    answer = (start+end)//2
    return answer

print(solution(nlist, m))