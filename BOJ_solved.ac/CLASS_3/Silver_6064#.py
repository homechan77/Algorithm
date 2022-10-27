# 카잉 달력

'''
# 시간 초과 O(m*n)
import sys; input = sys.stdin.readline

t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())
    m, n = 1, 1
    cnt = 1
    flag = False
    while not (m == x and n == y):
        if m == M and n == N:
            flag = True
            break
        if m < M:
            m += 1
        else:
            m = 1
        if n < N:
            n += 1
        else:
            n = 1
        cnt += 1
    
    if flag:
        print(-1)
    else:
        print(cnt)
'''
##--------------------------------------------------------------------------##
import sys; input = sys.stdin.readline

t = int(input())

# 유클리제 호제법(재귀)을 활용한 최소공약수 산출
def gcd(a, b):
    if a >= b:
        if a % b != 0:
            return gcd(b, a % b)
        else:
            return b
    else:
        if b % a != 0:
            return gcd(a, b % a)
        else:
            return a

# x를 고정한 상태에서 cnt를 늘리면서 해당 cnt의 N값을 확인한다.
# <x:y>가 유효하지 않은 표현이면, -1을 출력해야 하므로 결국 cnt가 M과 N의 최소공배수(lcm)를 초과하게 될 경우 -1을 출력하게 한다.
def solution(t):
    for _ in range(t):
        M, N, x, y = map(int, input().split())
        cnt = x
        flag = False
        lcm = M * N / gcd(M, N)
        while cnt <= lcm:
            Y = cnt % N
            if Y == 0:
                Y = N
            if Y == y:
                flag = True
                break
            cnt += M
        if flag:
            print(cnt)
        else:
            print(-1)

solution(t)
