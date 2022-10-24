# AC
# 출력 결과값들 사이에 공백이 있어서는 안된다. ex) [2, 1] (X), [2,1] (O)

import sys; input = sys.stdin.readline
from collections import deque

t = int(input())

def printing(arr):
    print('[', end='')
    for n, i in enumerate(arr):
        if n == len(arr)-1:
            print(i, end='')
        else:
            print(i, end='')
            print(',', end='')
    print(']')

for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    arrinput = input().rstrip()
    if arrinput == '[]':
        arr = []
    else:
        arr = deque(list(map(int, arrinput[1:-1].split(','))))
    check = False
    noti = False
    for i in p:
        if i == 'R':
            if check:
                check = False
            else:
                check = True
        else:
            if len(arr) == 0:
                print("error")
                noti =True
                break
            else:
                if check == True:
                    arr.pop()
                else:
                    arr.popleft()
    if not noti:
        if check == True:
            arr.reverse()
            printing(list(arr))
        else:
            printing(list(arr))