# 종이의 개수

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
array = []
# for _ in range(n):
    # array.append(list(map(int, input().split())))
array = [list(map(int, input().split())) for _ in range(n)]

##--------------------------------------------------------------------------##
# 시도1. 메모리 초과
# def is_one(arr):
#     discri = []
#     for i in arr:
#         if not (len(list(set(i))) == 1):
#             return False
#         else:
#             discri.append(i[0])
#     if len(list(set(discri))) == 1:
#         return True
#     else:
#         return False


# def solution(array):
#     result = {'-1':0, '0':0, '1':0}
#     queue = deque([array])
#     while queue:
#         pop = queue.popleft()
#         if is_one(pop):
#             num = pop[0][0]
#             result[str(num)] += 1
#         else:
#             splitn = len(pop) // 3
#             temp = [[], [], []]
#             tn = 0
#             for i in pop:
#                 one, two, three = i[0:splitn], i[splitn:(splitn*2)], i[(splitn*2):(splitn*3)]
#                 for nj, j in enumerate([one, two, three]):
#                     temp[nj].append(j)
#                 tn += 1
#                 if tn % splitn == 0:
#                     queue.extend(temp)
#                     temp = [[], [], []]
    
#     for i in list(result.values()):
#         print(i)

# solution(array)

##--------------------------------------------------------------------------##
# 시도2. 메모리 초과
def is_one(arr):
    discri = 0
    for n, i in enumerate(arr):
        if len(list(set(i))) == 1:
            if n == 0:
                discri = i[0]
            else:
                if i[0] != discri:
                    return False
        else:
            return False
    return True

def split(arr):
    splitarr = [[] for _ in range(9)]
    splitn = len(arr) // 3
    cnt = 0
    for n, i in enumerate(arr):
        num = (cnt+1)*3
        splitarr[num-3].append(i[0:splitn])
        splitarr[num-2].append(i[splitn:(splitn*2)])
        splitarr[num-1].append(i[(splitn*2):(splitn*3)])
        if (n+1) % splitn == 0:
            cnt += 1
    return splitarr

def solution2(array):
    result = {'-1': 0, '0': 0, '1': 0}
    queue = deque([array])
    while queue:
        pop = queue.popleft()
        if is_one(pop):
            result[str(pop[0][0])] += 1
        else:
            splitarr = split(pop)
            queue.extend(splitarr)
    
    for i in list(result.values()):
        print(i)

solution2(array)

##--------------------------------------------------------------------------##
# 정답자 코드 참조

# 분할정복(divide Conquer)-재귀

import sys

sys.setrecursionlimit(10**6)

input= sys.stdin.readline

N=int(input().rstrip())

board=[list(map(int,input().split())) for _ in range(N)]
zero=0
one=0
minus_one=0
def solve(y,x,n):
    global zero,one,minus_one
    # 종이가 모두 같은 수로 이루어져 있는지 확인
    init=board[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if board[i][j] != init:
                # 같은 수로 이루어져 있지 않다면, 9 등분을 합시다.
                for k in range(3):
                    for l in range(3):
                        solve(y+k*n//3,x+l*n//3,n//3)
                # 같지 않기 때문에, 이 loop는 종료해줍니다. 불필요한 반복을 하지 않습니다.
                return
    if init==0:
        zero+=1
    elif init==1:
        one+=1
    elif init==-1:
        minus_one+=1
    return

solve(0,0,N)

print(minus_one)
print(zero)
print(one)