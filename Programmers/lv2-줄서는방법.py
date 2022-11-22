# 줄 서는 방법
# import math
# math.factorial

def factorial(x):
    flist = [1]
    for i in range(1, x+1):
        flist.append(flist[-1]*i)
    return flist

def solution(n, k):
    flist = factorial(n-1)
    arr = [i for i in range(1, n+1)]
    k -= 1
    result = []

    while n > 0:
        q, r = k//flist[n-1], k%flist[n-1]
        result.append(arr[q])
        del arr[q]
        k = r
        n -= 1
    # answer = ''.join(map(lambda x: str(x), result))
    return result

n, k = 3, 5
print(solution(n, k))
# [3,1,2]
