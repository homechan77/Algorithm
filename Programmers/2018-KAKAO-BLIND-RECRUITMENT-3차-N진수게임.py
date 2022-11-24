# N진수 게임

def makelist(num, n):
    li = []
    while num > 0:
        q, r = num//n, num%n
        li.append(r)
        num = q
    li.reverse()
    return li

def solution(n, t, m, p):
    numdict = {}
    for i in range(16):
        if i > 9:
            numdict[i] = hex(i)[2].upper()
        else:
            numdict[i] = str(i)
    
    cnt = 1
    myturn = p
    num = 0
    result = []
    while True:
        if num in ([0, 1]):
            arr = [num]
        else:
            arr = makelist(num, n)
        for i in  arr:
            if cnt == myturn:
               result.append(numdict[i])
               myturn += m
            cnt += 1
            if len(result) == t:
                return ''.join(result)
        num += 1

n, t, m, p = 16, 16, 2, 1
print(solution(n, t, m, p))