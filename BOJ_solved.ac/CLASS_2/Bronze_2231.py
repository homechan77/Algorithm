n = int(input())

def solution(n):
    for i in range(n+1):
        ilist = list(str(i))
        a=0
        for j in ilist:
            a+=int(j)
        a+=i
        if a == n:
            return i
    return 0

print(solution(n))


