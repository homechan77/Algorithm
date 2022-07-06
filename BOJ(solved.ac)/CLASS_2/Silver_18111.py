import sys

n, m, b = map(int, sys.stdin.readline().split())
##--------------------------------------------------------------------------##
# 시도1. 시간 초과_64,000,000(256*500(n)*500(m))+α
# from collections import deque

# field = []
# for _ in range(n):
#     field.extend(list(map(int, sys.stdin.readline().split())))

# def solution(field, b):
#     fs = [0]*257
#     for i in field:
#         fs[i] += 1
#     fh = [i for i in range(len(fs)) if fs[i] != 0]
            
#     answerlist = []
#     for i in fh:
#         fieldcopy = field.copy()
#         bcopy = b
#         queue = deque(fieldcopy)
#         cnt = 0
#         alarm = False
#         while queue:
#             pop = queue.popleft()
#             if pop < i:
#                 cnt += (i-pop)
#                 bcopy -= (i-pop)
#             elif pop > i:
#                 cnt += (pop-i)*2
#                 bcopy += (pop-i)
                
#         if bcopy < 0:
#             alarm = True        
#         if alarm is not True:
#             answerlist.append([cnt, i])
    
#     answerlist = sorted(answerlist, key=lambda x: (x[0], -x[1]))
#     answer = " ".join(map(str, answerlist[0]))
#     return answer

# print(solution(field, b))
##--------------------------------------------------------------------------##
# 시도2. 성공
from collections import Counter

field = []
for _ in range(n):
    field.extend(list(map(int, sys.stdin.readline().split())))

def solution2(field, b):
    a = dict(Counter(field))
    aitems = a.items()
    akeys = list(a.keys())
    akeyslist = [i for i in range(min(akeys), max(akeys)+1)] # 최대/최소값 사이 중간값도 기준 높이가 될 수 있다.
    answerlist = []
    for i in akeyslist:
        cnt = 0
        bcopy = b
        for j in aitems:
            if i == j[0]:
                continue
            if i > j[0]:
                cnt += (i-j[0])*j[1]
                bcopy -= (i-j[0])*j[1]
            elif i < j[0]:
                cnt += (j[0]-i)*2*j[1]
                bcopy += (j[0]-i)*j[1]
        if bcopy >= 0:
            answerlist.append([cnt, i])
    
    answerlist = sorted(answerlist, key=lambda x: (x[0],-x[1]))
    answer = " ".join(map(str, answerlist[0]))
    return answer
    
print(solution2(field, b))