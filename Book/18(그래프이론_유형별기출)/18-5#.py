# 최종 순위(백준_3665)

import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

def solution(t):
    for _ in range(t):
        n = int(input())
        rank = list(map(int, input().split()))
        changeranknum = int(input())
        # 상대적인 등수가 바뀐 쌍의 경우, 앞의 원소가 뒤의 원소보다 등수가 높다는 뜻이 아니다
        # 말 그대로 기존 등수에서 두 원소의 상대적인 등수가 바뀌었다는 의미일 뿐
        changerank = [list(map(int, input().split())) for _ in range(changeranknum)]
        
        graph = [0] * (n+1)
        for i in range(n):
            graph[rank[i]] = rank[:i]
        
        for i in changerank:
            if i[1] in graph[i[0]]:
                graph[i[0]].remove(i[1])
                graph[i[1]].append(i[0])
            elif i[0] in graph[i[1]]:
                graph[i[1]].remove(i[0])
                graph[i[0]].append(i[1])

        queue = deque()
        indegree = [0] * (n+1)
        for i in range(1, n+1):
            indegree[i] = len(graph[i])    
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        alarm = False
        while queue:
            if len(queue) >= 2:
                alarm = True
                break
            pop = queue.popleft()
            result.append(pop)
            for i in range(1, n+1):
                if pop in graph[i]:
                    graph[i].remove(pop)
                    if len(graph[i]) == 0:
                        queue.append(i)  
        if alarm:
            print("?")
        elif len(result) != n:
            print("IMPOSSIBLE")
        else:
            answer = " ".join(map(lambda x:str(x), result))
            print(answer)
                
solution(t)        
        
