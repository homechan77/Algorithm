from collections import deque

# DFS
def solution_dfs(n, computers):
    visited = [False]*(n+1)
    
    graph = [0]
    for idx1, i in enumerate(computers):
        temp = []
        for idx2, j in enumerate(i):
            if j == 1 and idx1 != idx2:
                temp.append(idx2+1)
        graph.append(temp)            
            
    connectedlist = []
    
    for idx, a in enumerate(graph):
        temp = []
        if a == 0 or visited[idx] == True:
            continue
        def dfs(visited, graph, idx):
            visited[idx] = True
            temp.append(idx)
            for b in graph[idx]:
                if not visited[b]:
                    dfs(visited, graph, b)
        dfs(visited, graph, idx)
        connectedlist.append(temp)
    
    return len(connectedlist)

##--------------------------------------------------------------------------##

# BFS
def solution_bfs(n, computers):
    visited = [False]*(n+1)

    graph = [0]
    for idx1, i in enumerate(computers):
        temp = []
        for idx2, j in enumerate(i):
            if j == 1 and idx1 != idx2:
                temp.append(idx2+1)
        graph.append(temp)  
        
    connectedlist = []
    
    for idx, a in enumerate(graph):
        temp_2 = []
        if a== 0 or visited[idx] == True:
            continue
        def bfs(visited, graph, idx):
            queue = deque()
            queue.append(idx)
            while queue:
                t = queue.popleft()
                visited[t] = True
                temp_2.append(t)
                for x in graph[t]:
                    if not visited[x]:
                        queue.append(x)
        
        bfs(visited, graph, idx)
        
        connectedlist.append(temp_2)
    
    return len(connectedlist)
    
    
n = 3
computers =[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# print(solution_bfs(n, computers))

##--------------------------------------------------------------------------##
# update code(22.11.11.)
from collections import deque

def bfs(arr, n):    
    visited = [False] * n
    cnt = 0
    
    for i, x in enumerate(arr):
        if visited[i] == False:
            visited[i] = True
            queue = deque(x)
            while queue:
                pop = queue.popleft()
                visited[pop] = True
                for y in arr[pop]:
                    if visited[y] == False:
                        queue.append(y)
                        visited[y] = True
            cnt += 1
    return cnt

def solution(n, computers):
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] == 1:
                    arr[i].append(j)
    answer = bfs(arr, n)
    return answer