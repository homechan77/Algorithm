# 종이의 개수

# 시도1. 메모리 초과
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def is_one(arr):
    discri = []
    for i in arr:
        if not (len(list(set(i))) == 1):
            return False
        else:
            discri.append(i[0])
    if len(list(set(discri))) == 1:
        return True
    else:
        return False


def solution(array):
    result = {'-1':0, '0':0, '1':0}
    queue = deque([array])
    while queue:
        pop = queue.popleft()
        if is_one(pop):
            num = pop[0][0]
            result[str(num)] += 1
        else:
            splitn = len(pop) // 3
            temp = [[], [], []]
            tn = 0
            for i in pop:
                one, two, three = i[0:splitn], i[splitn:(splitn*2)], i[(splitn*2):(splitn*3)]
                for nj, j in enumerate([one, two, three]):
                    temp[nj].append(j)
                tn += 1
                if tn % splitn == 0:
                    queue.extend(temp)
                    temp = [[], [], []]
    
    for i in list(result.values()):
        print(i)

solution(array)