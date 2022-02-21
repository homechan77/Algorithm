# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return

"""
# 시도1 - 실패(출발점을 각각의 섬으로 설정하여 4개의 값을 도출하고 가장 작은 값을 return)
# 거쳐간 섬이 있는 경우(사이클이 발생하는 경우) 해당 섬을 제외해야 하는데 이럴경우 과도한 반복문이 형성된다.
def solution(n, costs):
    
    costscopy = costs.copy()
    for i in costs:
        costscopy.append([i[1],i[0],i[2]])
    
    recost = []
    [recost.append([]) for _ in range(n)]
    for j in costscopy:
        recost[j[0]].append([j[1],j[2]])
    
    answerlist = []
    
    for k in range(n):
        count = 0
        
        numlist = [num for num in range(n)]
        while numlist:
            numlist.pop(k)
            a = min(recost[k], key=lambda x:x[1]) if a[0]
            if a[0] 
            count += a[1]
            k = a[0]
            if recost[k]
            
            
    # 거처간 섬의 경우 제외를 해야 하는데...
            
    return max(recost[0], key=lambda x:x[1])[0]

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))
"""
"""
##--------------------------------------------------------------------------##
# <서로소 집합 알고리즘 구현>
import sys

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i
    
# find 연산
def find_parent(parent, x):
    # 부모노드와 자식노드가 같지 않다면 => 부모노드가 따로 있다는 의미니까
    if parent[x] != x:
        return find_parent(parent, parent[x]) # 그 부모노드를 자식노드로 하는 또다른 자식노드 탐색
    return x
    # 위 코드의 개선된 버전
    # if parent[x] != x:
    #     parent[x] = find_parent(parent, parent[x])
    # return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
for _ in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)
    
print('# 각 원소의 루트 노드들: ', end='')
for i in range(1, v+1):
    root = find_parent(parent, i)
    print(root, end=' ')
print()
print('# 각 원소의 직계 부모 노드들: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
    
# 사이클 판별
cycle = False
for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 존재합니다')
else:
    print('사이클이 존재하지 않습니다')
##--------------------------------------------------------------------------##
# <크루스칼 알고리즘 구현>
import sys

v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))
    
edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost
"""
##--------------------------------------------------------------------------##
# 시도2 - 위의 코드를 참조
# 최소 신장 트리 알고리즘 중 크루스칼 알고리즘 활용

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a > b:
        parent[x] = b
        # 뒤이어 정의된 루트노드 관계가 앞서 정의된 루트노드 관계에 영향을 미칠 경우, 앞선 루트노드 관계를 이후의 루트관계를 참고하여 재정립하여 준다. 
        for pp in range(len(parent)):
            if parent[pp] == a:
                parent[pp] = b
    else:
        parent[y] = a
        for pp in range(len(parent)):
            if parent[pp] == b:
                parent[pp] = a


def solution(n, costs):
    # 간선간 비용을 기준으로 오름차수 정렬
    costs.sort(key=lambda x:x[-1])
    
    # 부모 테이블 생성
    parent = [p for p in range(n)]
    
    answer_cost = 0
    
    for i in range(len(costs)):
        a, b, cost = costs[i][0], costs[i][1], costs[i][2]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            
            answer_cost += cost

        
    return answer_cost

n = 5
costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]
print(solution(n, costs))

##--------------------------------------------------------------------------##
# # 시도3 - 정답자 코드 1
# def solution(n, costs):
#     answer = 0
#     costs.sort(key = lambda x: x[-1]) 
#     link = set([costs[0][0]])

#     # Kruskal 알고리즘으로 최소 비용 구하기
#     while len(link) != n:
#         for v in costs:
#             if v[0] in link and v[1] in link:
#                 continue
#             if v[0] in link or v[1] in link:
#                 link.update([v[0], v[1]])
#                 answer += v[2]
#                 break
                
#     return answer

# n = 5
# costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]
# print(solution(n, costs))

##--------------------------------------------------------------------------##
# 정답자 코드 2
# uf = []

# def find(a):
#     if uf[a] < 0:
#         return a
#     uf[a] = find(uf[a])
#     return uf[a]

# def merge(a, b):
#     a = find(a)
#     b = find(b)
#     if a == b:
#         return False
#     uf[b] = a
#     return True

# def solution(n, costs):
#     global uf
#     uf = [-1 for _ in range(n)]
#     costs.sort(key = lambda x:x[-1])
#     total, cnt = 0, 0
#     for a, b, w in costs:
#         if merge(a, b):
#             total += w
#             cnt += 1
#             if cnt == n-1:
#                 break
#     return total

# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# print(solution(n, costs))