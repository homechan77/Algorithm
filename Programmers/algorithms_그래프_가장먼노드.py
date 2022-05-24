from collections import deque, defaultdict

def solution(n, edge):
    visited = [False]*(n+1)
    start = 1
    nodedict = defaultdict(list)
    for i in edge:
        nodedict[i[0]].append(i[1])
        nodedict[i[0]].sort()
        nodedict[i[1]].append(i[0])
        nodedict[i[1]].sort()
    
    count = 0
    queue = deque([(count, start)])
    visited[start] = True
    
    answerdict = defaultdict(list)
    
    while queue:
        pop = queue.popleft()
        answerdict[pop[0]].append(pop[1])
        for j in nodedict[pop[1]]:
            if visited[j] == False:
                visited[j] = True
                counting = pop[0]+1
                queue.append((counting, j))
    
    answer = len(answerdict[max(answerdict.keys())])        
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))