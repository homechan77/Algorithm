import math

n = int(input())
nlist = list(map(int, input().split()))

def solution(n, nlist):
    answer = 0
    for i in range(n):
        if nlist[i]==0 or nlist[i]==1:
            continue
        condition = True
        for j in range(2, int(math.sqrt(nlist[i]))+1):
            if nlist[i]%j == 0:
                condition = False
                break
            
        if condition == True:
            answer += 1
    
    return answer

print(solution(n, nlist))
