from collections import deque

tn = int(input())
tlist = []
for i in range(tn):
    m, n = map(int, input().split())
    tmp = list(map(int, input().split()))
    labeltmp = []
    for j in range(m):
        if j==n:
            labeltmp.append((tmp[j], 't'))
        else:
            labeltmp.append((tmp[j], 'f'))
    tlist.append(labeltmp)

def solution(tlist):
    for i in range(tn):
        answer = 0
        queue = deque(tlist[i])
        while True:
            pop = queue.popleft()
            # 1. max()
            if len(queue) == 0:
                answer+=1
                print(answer)
                break
            if pop[0] < max(list(map(lambda x: x[0], queue))):
                queue.append(pop)
            else:
                answer += 1
                if pop[1] == 't':
                    print(answer)
                    break
            
            # 2. 반복문 비교
            # cnt = 0
            # for j in range(len(queue)):
            #     if queue[j][0] > pop[0]:
            #         queue.append(pop)
            #         break
            #     else:
            #         cnt+=1
            
            # if cnt == len(queue):
            #     answer += 1
            #     if pop[1] == 't':
            #         print(answer)
            #         break

solution(tlist)
