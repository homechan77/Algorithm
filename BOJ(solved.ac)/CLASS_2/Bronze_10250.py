# H, W, N, 세 정수를 포함하고 있으며 
# 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님

import sys

t = int(sys.stdin.readline())
tlist = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

def solution(tlist):
    for i in tlist:
        h, w, n = i[0], i[1], i[2]
        cnt = 0
        alarm = False
        for x in range(w):
            for y in range(h):
                if x+1 < 10:
                    answer = str(y+1)+'0'+str(x+1)
                else:
                    answer = str(y+1)+str(x+1)
                cnt += 1
                if cnt == n:
                    answer = int(answer)
                    print(answer)
                    alarm = True
                    break
            if alarm is True:
                break
    
solution(tlist)