# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    # 만약 더 섭취해야 할 음식이 없다면 -1을 반환
    if sum(food_times) <= k:
        return -1
    
    # 우선순위 큐에 (음식 시간, 음식 번호) 저장
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0
    previous = 0
    lenght = len(food_times)
    
    # (남은 음식 개수 x '?'음식 시간) = '?'음식을 다먹는 데 걸리는 시간
    # q[0][0]-previous -> 다음 음식의 남은 시간
    while sum_value + ((q[0][0]-previous)*lenght) <= k:
        now = heapq.heappop(q)[0] # 음식 시간
        sum_value += (now-previous)*lenght
        lenght -= 1
        previous = now
    
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % lenght][1]

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))

# food_times=[4,2,3,6,7,1,5,8] k=16 answer = 3
# food_times=[4,2,3,6,7,1,5,8] k=27 answer = 5
    