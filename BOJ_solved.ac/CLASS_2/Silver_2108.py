import sys
from collections import defaultdict, Counter

n = int(sys.stdin.readline())
nlist = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=False)

def solution(n, nlist):
    for i in range(4):
        if i==0:
            print(round(sum(nlist) / n))
        elif i==1:
            p = (n//2)
            print(nlist[p])
        elif i==2:
            if n==1:
                print(nlist[0])
                continue
            
            # tdict = defaultdict(int)
            # for j in nlist:
            #     tdict[j]+=1
            # tlist = sorted(tdict.items(), key=lambda x:x[1], reverse=True)
            # if tlist[0][1] == tlist[1][1]:
            #     print(tlist[1][0])
            # else:
            #     print(tlist[0][0])
            
            # Counter 클래스 사용
            tlist = Counter(nlist).most_common()
            if tlist[0][1] == tlist[1][1]:
                print(tlist[1][0])
            else:
                print(tlist[0][0])
            
        elif i==3:
            print(nlist[-1]-nlist[0])

solution(n, nlist)