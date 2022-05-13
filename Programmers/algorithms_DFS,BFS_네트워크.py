def solution(n, computers):
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

n = 3
computers =[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))