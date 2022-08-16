import sys

n = int(sys.stdin.readline())

def solution(n):
    tmp = []
    for _ in range(n):
        order = sys.stdin.readline().strip()
        if order[0:4] == 'push':
            order, number = order.split()
        
        if order == 'push':
            tmp.append(int(number))
        elif order == 'pop':
            if len(tmp) == 0:
                print(-1)
            else:
                popn = tmp.pop()
                print(popn)
        elif order == 'size':
            print(len(tmp))
        elif order == 'empty':
            if len(tmp) == 0:
                print(1)
            else:
                print(0)
        elif order == 'top':
            if len(tmp) == 0:
                print(-1)
            else:
                print(tmp[-1])
solution(n)