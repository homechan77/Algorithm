import sys

t = int(sys.stdin.readline())
testcase = [int(sys.stdin.readline()) for _ in range(t)]
##--------------------------------------------------------------------------##
# 시도1. 시간 초과
answer = [0, 0]

def fibo(n):
    global answer
    if n == 0:
        answer[0]+=1
        return 0
    elif n == 1:
        answer[1]+=1
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def solution(testcase):
    global answer
    for i in testcase:
        fibo(i)
        print(" ".join(map(str, answer)))
        answer = [0,0]

# solution(testcase)

##--------------------------------------------------------------------------##
# 시도2. 성공_메모이제이션
ma = [[0,0]]*41

def fibo2(n):
    global ma
    if ma[n] != [0,0]:
        return ma[n]
    if n==0:
        ma[0] = [1,0]
        return ma[0]
    elif n==1:
        ma[1] = [0,1]
        return ma[1]
    else:
        ma[n-1] = fibo2(n-1)
        ma[n-2] = fibo2(n-2)
        ma[n] = [ma[n-1][0] + ma[n-2][0], ma[n-1][1] + ma[n-2][1]]
        return ma[n]

def solution2(testcase):
    global ma
    for i in testcase:
        fibo2(i)
        print(" ".join(map(str, ma[i])))
        ma = [[0,0]]*41

solution2(testcase)