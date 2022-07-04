import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
nlist = [i+1 for i in range(n)]

def solution(nlist, k):
    answer = []
    queue = deque(nlist)
    cnt = 0
    while queue:
        if len(queue) == 1:
            poplast = queue.popleft()
            answer.append(poplast)
            break
        pop = queue.popleft()
        cnt += 1
        if cnt == k:
            answer.append(pop)
            cnt = 0
        else:
            queue.append(pop)
    
    # print('<', end='')
    # for j in range(n):
    #     if j == n-1:
    #         print(answer[j], end='')
    #         break
    #     else:
    #         print(answer[j], end='')
    #         print(',', end=' ')
    # print('>')
    print("<"+', '.join(map(str, answer))+">")
    

solution(nlist, k) 