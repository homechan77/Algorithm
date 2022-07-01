import sys
from collections import Counter

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))

# 시도1. 시간 초과
def solution(nlist, mlist):
    nlistcount = Counter(nlist).most_common()
    for i in mlist:
        alarm = False
        for j in nlistcount:
            if i== j[0]:
                print(j[1], end=" ")
                alarm = True
                break
        if alarm is True:
            continue
        else:
            print(0, end=" ")
    
# solution(nlist, mlist)
##--------------------------------------------------------------------------##
# 시도2. 이진 탐색_성공
def solution2(nlist, mlist):
    nlistcount = sorted(Counter(nlist).most_common(), key=lambda x: x[0])
    for i in mlist:
        start = 0
        end = len(nlistcount)-1
        alarm = False
        while start <= end:
            mid = (start+end)//2
            if nlistcount[mid][0] == i:
                print(nlistcount[mid][1], end=" ")
                alarm = True
                break
            elif nlistcount[mid][0] < i:
                start = mid+1
            elif nlistcount[mid][0] > i:
                end = mid-1
                
        if alarm is not True:        
            print(0, end=" ")
            
solution2(nlist, mlist)