import sys
from collections import deque

n = int(sys.stdin.readline())

def solution(n):
    queue = deque([])
    for _ in range(n):
        order = sys.stdin.readline().strip()
        if order[0:4] == 'push':
            order, number = order.split()
        
        if order == 'push':
            queue.append(int(number))
        elif order == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                pop = queue.popleft()
                print(pop)
        elif order == 'size':
            print(len(queue))
        elif order == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif order == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif order == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])

solution(n)