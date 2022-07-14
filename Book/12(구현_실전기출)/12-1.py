import sys

n = list(sys.stdin.readline().strip())
def solution(n):
    nlen = len(n)//2
    a = n[:nlen]
    b = n[nlen:]
    asum = sum(map(lambda x: int(x), a))
    bsum = sum(map(lambda x: int(x), b))
    if asum == bsum:
        return 'LUCKY'
    else:
        return 'READY'

print(solution(n)) 