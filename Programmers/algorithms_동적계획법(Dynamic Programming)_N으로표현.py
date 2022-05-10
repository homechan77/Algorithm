# N과 사칙연산만을 사용하여 number를 계산할 경우 N 사용횟수의 최솟값을 return
# 최소값이 8보다 크면 -1을 return

"""
def solution(N, number):
    res = 8
    dp = [0]*res
    dp[0] = [N]
    if N == number:
        return 1
    for i in range(1, res):
        templist = []
        cn = int(str(N)*(i+1))
        if cn == number:
            return i+1
        templist.append(cn)
        for j in range(len(dp[i-1])):
            for k in ["+", "-", "*", "/"]:
                if k == "+":
                    p = dp[i-1][j] + N
                    if p == number:
                        return i+1
                    else:  
                        templist.append(p)
                elif k == "-":
                    m1 = dp[i-1][j] - N
                    m2 = N - dp[i-1][j]
                    if m1 == number or m2 == number:
                        return i+1
                    else:
                        templist.append(m1)
                        templist.append(m2)
                elif k == "*":
                    c = dp[i-1][j] * N
                    if c == number:
                        return i+1
                    else:
                        templist.append(c)
                else:
                    d1 = dp[i-1][j] // N
                    try:
                        d2 = N // dp[i-1][j]
                    except ZeroDivisionError:
                        d2 = 0
                    if d1 == number or d2 == number:
                        return i+1
                    else:
                        templist.append(d1)
                        templist.append(d2)
            dp[i]=templist                            
    
    return -1
"""


def solution(N, number):
    dp = [0,[N]]
    if N==number:
        return 1
    for i in range(2,9):
        templist = []
        
        cn = int(str(N)*i)
        templist.append(cn)
        
        for j in range(1, i//2+1):
            for x in dp[j]:
                for y in dp[i-j]:
                    templist.append(x+y)
                    templist.append(x-y)
                    templist.append(y-x)
                    templist.append(x*y)
                    if y != 0:
                        templist.append(x/y)
                    if x != 0:
                        templist.append(y/x)
        
        if number in templist:
            return i
        
        dp.append(templist)
    
    return -1

N = 6
number = 65
print(solution(N,number))
