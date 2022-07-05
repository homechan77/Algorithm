import sys
from collections import deque

k = int(sys.stdin.readline())
klist = [int(sys.stdin.readline()) for _ in range(k)]

def solution(klist):
    queue = deque(klist)
    answerlist = []
    while queue:
        pop = queue.popleft()
        if pop != 0:
            answerlist.append(pop)
        else:
            answerlist.pop()
    answer = sum(answerlist)
    return answer

print(solution(klist))