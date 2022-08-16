from collections import deque

nlist = [i+1 for i in range(int(input()))]

def solution(nlist):
    queue = deque(nlist)
    while len(queue) > 1:
        queue.popleft()
        pop2 = queue.popleft()
        queue.append(pop2)
    return queue[0]

print(solution(nlist))
