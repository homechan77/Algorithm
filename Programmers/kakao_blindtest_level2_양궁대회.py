# # DFS(깊이 우선 탐색)
# ef dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)    

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False]*9

# print(dfs(graph, 1, visited))

##--------------------------------------------------------------------------##

# [참고] https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-Python
# dfs 활용 완전 탐색 방법

import copy

maxscorediff = 0
answer = []

def caldiff(info, myshots):
    appeachscore, lionscore = 0,0
    for i in range(11):
        if (info[i], myshots[i]) == (0, 0):
            continue
        if info[i] >= myshots[i]:
            appeachscore += (10-i)
        else:
            lionscore += (10-i)
    return lionscore - appeachscore


def dfs(info, myshots, n, i):
    global maxscorediff, answer
    if i == 11:
        if n != 0:
            myshots[10] = n
        scorediff = caldiff(info, myshots)
        if scorediff <= 0:
            return
        result = copy.deepcopy(myshots)
        if scorediff > maxscorediff:
            maxscorediff = scorediff
            answer = [result]
            return
        if scorediff == maxscorediff:
            answer.append(result)
        return


    if info[i] < n:
        myshots.append(info[i]+1)
        dfs(info, myshots, n-(info[i]+1), i+1)
        myshots.pop()

    myshots.append(0)
    dfs(info, myshots, n, i+1)
    myshots.pop()



def solution(n, info):
    global maxscorediff, answer
    dfs(info, [], n, 0)
    if answer == []:
        return [-1]
    answer.sort(key=lambda x:x[::-1], reverse=True)
    return answer[0]

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))
