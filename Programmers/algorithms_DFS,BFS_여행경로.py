# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.

from collections import defaultdict

def solution(tickets):

    routes = {}
    for i in range(len(tickets)):
        if i == 0:
            routes[tickets[i][0]] = []
            continue
        if tickets[i][0] not in routes:
            routes[tickets[i][0]] = []
    
    for j in tickets:
        routes[j[0]].append(j[1])
        routes[j[0]].sort()
    
    
    def dfs(routes):
        stack = ["ICN"]
        path = []
        while len(stack) > 0:
            top = stack[-1]
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]
    
    path = dfs(routes)
    
    return path
    
    # def dfs(destination):
    #     nonlocal visited, answer, path 
    
    #     temp = destination[answer[-1]][0]
    #     destination[answer[-1]].remove(temp)
        
    #     if temp in destination:
    #         answer.append(temp)
    #         visited += 1
    #         if visited == lentickets:
    #             return
    #         dfs(destination)
    #     else:
    #         path.append(temp)
    #         visited += 1
    #         dfs(destination)

    # dfs(destination)


tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# tickets = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))
