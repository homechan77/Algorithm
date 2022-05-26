# 플로이드-워셜 알고리즘
# n명의 선수가 존재할 때, n-1명의 다른 선수들과의 승패를 확실하게 알 수 있을 때 순위가 정해진다.
# a->b / b->c = a->c

def solution(n, results):
    inf = int(1e9)
    graph = [[inf]*(n+1) for _ in range(n+1)]

    for i in results:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = -1
    
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == graph[k][b] and graph[a][b] not in [1,-1]:
                    graph[a][b] = graph[a][k]
                    
    for a in range(n+1):
        for b in range(n+1):
            if a==b:
                graph[a][b] = 0
    
    answer = 0
    for x in graph:
        count = 0
        for y in enumerate(x):
            if y[0] == 0:
                continue
            if y[1] != inf:
                count += 1
        if count == n:
            answer += 1
        
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
# return: 2