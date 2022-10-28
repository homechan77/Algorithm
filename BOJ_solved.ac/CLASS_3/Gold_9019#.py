# DSLR

'''
# 시도1. 실패
import sys; input = sys.stdin.readline
from collections import deque
import copy

tn = int(input())

def makeint(lis):
    d1, d2, d3, d4 = lis
    n = (((int(d1) * 10 + int(d2)) * 10 + int(d3)) * 10 + int(d4))
    return n

def makecl(case):
    a = ['0', '0', '0', '0']
    flag = False
    if case[0] == '-':
        caselist = list(case)[1:]
        flag = True
    else:
        caselist = list(case)
    for i in range(1, 5):
        pop = caselist.pop()
        if flag == True:
            a[-i] = '-'+pop
        else:
            a[-i] = pop
        if len(caselist) == 0:
            return a

def D(cl):
    c = makeint(cl)
    dc = c*2
    if dc > 9999:
        dc = dc % 10000
    listdc = makecl(str(dc))
    return listdc, dc

def S(cl):
    c = makeint(cl)
    sc = c-1
    if sc == 0:
        sc = 9999
    listsc = makecl(str(sc))
    return listsc, sc

def L(cl):
    a, b, c, d = cl
    listlc = [b, c, d, a]
    lc = makeint(listlc)
    return listlc, lc

def R(cl):
    a, b, c, d = cl
    listrc = [d, a, b, c]
    rc = makeint(listrc)
    return listrc, rc

def bfs(cl, answer):
    queue = deque([(cl, [])])
    while queue:
        cl, command = queue.popleft()
        for i in range(4):
            commandcopy = copy.deepcopy(command)
            if i == 0:
                commandcopy.append('D')
                listd, intd = D(cl)
                if intd == answer:
                    return commandcopy
                queue.append((listd, commandcopy))
            elif i == 1:
                commandcopy.append('S')
                lists, ints = S(cl)
                if ints == answer:
                    return commandcopy
                queue.append((lists, commandcopy))
            elif i == 2:
                commandcopy.append('L')
                listl, intl = L(cl)
                if intl == answer:
                    return commandcopy
                queue.append((listl, commandcopy))
            else:
                commandcopy.append('R')
                listr, intr = R(cl)
                if intr == answer:
                    return commandcopy
                queue.append((listr, commandcopy))

def solution(tn):
    for _ in range(tn):
        case, answer = input().rstrip().split()
        answer = int(answer)
        cl = makecl(case)
        commandline = ''.join(bfs(cl, answer))
        print(commandline)

solution(tn)
'''
##--------------------------------------------------------------------------##
# 시도2. 정답자 코드 참조
# key_point(1) visited 활용
# key_point(2) 좌,우 회전 함수 oper_L(), oper_R()

import sys; input = sys.stdin.readline
from collections import deque

def oper_D(n):
    res = n * 2
    if res > 9999:
        res %= 10000
    return res

def oper_S(n): 
    res = n
    if res == 0: return 9999
    res -= 1
    return res

def oper_L(n):
    front = n % 1000
    back = n // 1000
    res = front*10 + back
    return res


def oper_R(n):
    front = n % 10
    back = n // 10
    res = front*1000 + back
    return res

def bfs(s, t):
    queue = deque()
    visited = set() # logn
    queue.append((s, ""))
    visited.add(s)
    while queue:
        cur_num, oper = queue.popleft()
        if cur_num == t:
            print(oper)
            return
        tmp = oper_D(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"D"))
        tmp = oper_S(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"S"))
        tmp = oper_L(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"L"))
        tmp = oper_R(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"R"))

for _ in range(int(input())):
    start, target = map(int, input().split())
    bfs(start, target)