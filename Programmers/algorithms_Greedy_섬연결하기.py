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

# 시도2 - 
# 최소 신장 트리 알고리즘 중 크루스칼 알고리즘 활용
# 참고 동영상(https://youtu.be/Gj7s-Nrt1xE)

uf = []

def find(a):
    if uf[a] < 0:
        return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    uf[b] = a
    return True

def solution(n, costs):
    global uf
    uf = [-1 for _ in range(n)]
    costs.sort(key = lambda x:x[-1])
    total, cnt = 0, 0
    for a, b, w in costs:
        if merge(a, b):
            total += w
            cnt += 1
            if cnt == n-1:
                break
    return total

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))