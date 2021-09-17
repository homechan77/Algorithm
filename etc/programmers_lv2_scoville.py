#프로그래머스_lv2_더 맵게
"""
#정확성-일부 런타임에러 / 효율성-시간초과
def solution(scoville, K):
    count = 0
    while min(scoville) < K:
        scoville = sorted(scoville)
        count += 1
        a = scoville[0] + (scoville[1]*2)
        scoville.append(a)
        del scoville[:2]
    return count

scoville = [1, 2, 3, 9, 10, 12]	
K = 7

print(solution(scoville, K))
"""
#우선순위 큐의 사용
import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while 1:
        if len(scoville) <= 1 and scoville[0] < K:
            count = -1
            break
        if scoville[0] >= K:
            break
        new_num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_num)
        count += 1
    
    return count

scoville = [1, 2, 3, 9, 10, 12]	
K = 7

print(solution(scoville, K))