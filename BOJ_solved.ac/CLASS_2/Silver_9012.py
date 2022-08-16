import sys
from collections import deque

n = int(sys.stdin.readline())
nlist = [sys.stdin.readline() for _ in range(n)]

def solution(nlist):
    for  i in nlist:
        ilist = list(i)
        ilist.pop() #'\n' 제거
        queue = deque(ilist)
        tmp = []
        alarm = False
        while queue:
            pop = queue.popleft()
            if pop == '(':
                tmp.append(pop)
            else:
                if len(tmp)==0:
                    print('NO')
                    alarm = True
                    break
                else:
                    tmp.pop()
        if len(queue)==0 and len(tmp)==0:
            if alarm is True:
                continue
            else:
                print('YES')
        else:
            if alarm is True:
                continue
            else:
                print('NO')

solution(nlist)
    