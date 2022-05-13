# 스택: FILO(First In Last Out) / append(), pop() / 재귀 함수 / DFS
# 큐: FIFO(First In First Out) / deque / BFS

# DFS_재귀함수
def solution(numbers, target):
    
    n=len(numbers)
    answer=0
    
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
            
    dfs(0,0)
    
    return answer

# DFS_stack
def solution3(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
    

# BFS_queue
from collections import deque

def solution2(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    
    queue.append([numbers[0], 0]) # case1: number[0]이 양수로 시작하는 경우
    queue.append([-1*numbers[0], 0]) # case2: number[0]이 음수로 시작하는 경우
    
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    
    return answer


numbers = [1, 1, 1, 1, 1]	
target = 3
# print(solution(numbers, target))
