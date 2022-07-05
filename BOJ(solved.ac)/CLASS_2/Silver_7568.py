import sys
from collections import deque

n = int(sys.stdin.readline())
nlist = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(nlist):
    answerlist = []
    queue = deque(nlist)
    for _ in range(len(nlist)):
        cnt = 0
        pop = queue.popleft()
        for i in queue:
            if i[0] > pop[0] and i[1] > pop[1]:
                cnt += 1
        answerlist.append(cnt+1)
        queue.append(pop)
    answer = " ".join(map(str, answerlist))
    return answer

print(solution(nlist))