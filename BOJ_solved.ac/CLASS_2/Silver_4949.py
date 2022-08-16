import sys
from collections import deque

def tc():
    tlist = []
    while True:
        a = input()
        if a == '.':
            return tlist
        tlist.append(list(a.split()))


def solution(testcase):
    for i in testcase:
        if i == '.':
            print('yes')
            break
        queue = deque(i)
        tmp = []
        alarm = False
        while queue:
            pop = queue.popleft()
            for j in list(pop):
                if j == '[' or j == '(':
                    tmp.append(j)
                elif j == ']':
                    if len(tmp)==0 or tmp[-1] != '[':
                        print('no')
                        alarm = True
                        break
                    tmp.pop()
                elif j == ')':
                    if len(tmp)==0 or tmp[-1] !='(':
                        print('no')
                        alarm = True
                        break
                    tmp.pop()
            if alarm is True:
                break
        if alarm is False and len(tmp)==0:
            print('yes')
        elif alarm is False and len(tmp)>0:
            print('no')

testcase = tc()
solution(testcase)
                    