# 집합

import sys; input = sys.stdin.readline

m = int(input())
x = [False] * 21

for _ in range(m):
    Str = input().rstrip()
    if Str != 'all' and Str != 'empty':
        Str, Num = Str.split()
        Num = int(Num)
    if Str == 'add':
        if x[Num] == False:
            x[Num] = True
    elif Str == 'remove':
        if x[Num] == True:
            x[Num] = False
    elif Str == 'toggle':
        if x[Num] == False:
            x[Num] = True
        else:
            x[Num] = False
    elif Str == 'all':
        x = [True] * 21
    elif Str == 'empty':
        x = [False] * 21
    else:
        if x[Num] == True:
            print(1)
        else:
            print(0)