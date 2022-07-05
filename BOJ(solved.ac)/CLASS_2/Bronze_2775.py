import sys

t = int(sys.stdin.readline())
tcase = []
for _ in range(t):
    tmp = []
    for _ in range(2):
        tmp.append(int(sys.stdin.readline()))
    tcase.append(tmp)

# 해당 층까지의 전체 리스트 원소(호수별 인원)를 산출하고 요구하는 호수를 찾아 정답 출력
def solution(tcase):
    for i in tcase:
        floor = [[_ for _ in range(1, 15)]]
        for j in range(i[0]):
            ftmp = [1]
            j += 1
            for k in range(14):
                if k==0:
                    continue
                ftmp.append(ftmp[k-1]+floor[j-1][k])
            floor.append(ftmp)
        print(floor[i[0]][i[1]-1])
        
        
# 각 층마다 요구하는 호수까지만 원소 출력 후 해당 층에 도달하면 정답 출력
def solution2(tcase):
    for i in tcase:
        floor = [[_ for _ in range(1, 15)]]
        for j in range(i[0]):
            ftmp = [1]
            if i[1] == 1:
                floor.append(ftmp)
                continue
            j += 1
            alarm = False
            for k in range(14):
                if k==0:
                    continue
                ftmp.append(ftmp[k-1]+floor[j-1][k])
                if j==i[0] and len(ftmp)==i[1]:
                    floor.append(ftmp)
                    alarm = True
                    break
                if len(ftmp)==i[1]:
                    break
            if alarm is False:
                floor.append(ftmp)
        print(floor[-1][-1])
              
solution2(tcase)