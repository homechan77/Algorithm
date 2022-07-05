import sys

n = int(sys.stdin.readline())

# 시도1. dfs_시간 초과.
visited = [0]*(n+1)
cnt = 0
answer = 99999

def dfs(n, visited):
    global cnt, answer
    cnt += 1
    if visited[n] != 0:
        cnt -= 1
        return visited[n]
    tmp = []
    for i in [n-5, n-3]:
        if i == 0:
            if cnt < answer:
                answer = cnt
                tmp.append(0)
            else:
                tmp.append(0)
        elif i < 0:
            tmp.append(99999)
        else:
            dfs(i, visited)
            tmp.append(visited[i])
    
    visited[n] = min(tmp)
    cnt -= 1
    return answer

def solution(a):
    if a == 99999:
        return -1
    else:
        return a

# a = dfs(n, visited)
# print(solution(a))

##--------------------------------------------------------------------------##
# 시도2. greedy_성공.
def solution2(n):
    count = 0
    while n >= 0:
        if n % 5==0:
            count += int(n//5)
            return count
        n -= 3
        count += 1
    else:
        return -1

print(solution2(n))