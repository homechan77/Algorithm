# 케빈 베이컨의 6단계 법칙

import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
conn_info = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for i in conn_info:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
graph = list(map(lambda x: list(set(x)), graph))

result = [50001] * (n+1)

def dfs(target, result, cnt):    
    cnt += 1
    if cnt < result[target]:
        result[target] = cnt
    else:
        return
    for i in graph[target]:
        dfs(i, result, cnt)
    return result

def solution(n):
    answer = []
    for i in range(1, n+1):
        result_s = copy.deepcopy(result)
        cnt = -1
        rs = dfs(i, result_s, cnt)
        rssum = sum(map(lambda x: x, rs[1:]))
        answer.append([i, rssum])
    answer = sorted(answer, key=lambda x: (x[1], x[0]))
    return answer[0][0]

print(solution(n))