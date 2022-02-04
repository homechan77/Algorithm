#1. 현재 태스크 종료 범위 안에 요청된 태스크 중 길이가 짧은 태스크 부터 수행
#2. 요청 시간이 같다면 길이가 짧은 태스크부터 수행
# import heapq

# def solution(jobs):
#     heap = []
#     for i in jobs:
#         heapq.heappush(heap, [i[1], i[0]])
    
#     answer = 0
#     # time = heap[0][0] - heap[0][1]
#     time = 0
#     lenheap = len(heap) 
#     while heap:
        
#         temp =  heapq.heappop(heap)
        
#         answer += (time-temp[1]) + temp[0]
        
#         time += temp[0]
        
#     return answer // lenheap

# jobs = [[0, 3], [1, 9], [2, 6]]
# print(solution(jobs))



import heapq

def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
            
    return answer // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))