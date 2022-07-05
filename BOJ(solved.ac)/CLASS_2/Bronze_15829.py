import sys
from collections import defaultdict

l = int(sys.stdin.readline())
lstr = list(sys.stdin.readline().strip())
r = 31
m = 1234567891

def solution(lstr, r, m):
    tmpdict = defaultdict(int)
    cnt = 1
    for i in range(97, 123):
        tmpdict[chr(i)] = cnt
        cnt += 1
    
    answer = 0
    for j in range(len(lstr)):
        answer += tmpdict[lstr[j]]*(r**j)
    
    return answer%m

print(solution(lstr, r, m))