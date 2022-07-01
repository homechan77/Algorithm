import sys
from collections import deque

n = int(sys.stdin.readline())

def solution(n):
    deck = deque([])
    for _ in range(n):
        order = sys.stdin.readline().strip()
        if order[:10] == 'push_front' or order[:9] == 'push_back':
            order, number = order.split()

        if order == 'push_front':
            deck.reverse()
            deck.append(int(number))
            deck.reverse()
        elif order == 'push_back':
            deck.append(int(number))
        elif order == 'pop_front':
            if len(deck)==0:
                print(-1)
            else:
                popf = deck.popleft()
                print(popf)
        elif order == 'pop_back':
            if len(deck)==0:
                print(-1)
            else:
                popb = deck.pop()
                print(popb)
        elif order == 'size':
            print(len(deck))
        elif order == 'empty':
            if len(deck) == 0:
                print(1)
            else:
                print(0)
        elif order == 'front':
            if len(deck)==0:
                print(-1)
            else:
                print(deck[0])
        elif order == 'back':
            if len(deck)==0:
                print(-1)
            else:
                print(deck[-1])

solution(n)
            