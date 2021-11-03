#deque를 활용하지 않은 코드

def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    sec = 0

    while q:
        sec += 1
        q.pop(0)

        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec

##--------------------------------------------------------------------------##
#deque를 활용한 코드

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    answer = 1
    weights = deque([])
    times = deque([])

    truck = iter(truck_weights)
    weights.append(next(truck, False))
    times.append(0)
    cur = next(truck, False)

    while weight:
        answer += 1
        times = deque(t+1 for t in times)
        
        if times[0] == bridge_length:
            times.popleft()
            weight.popleft()

        if cur and len(times)+1 <= bridge_length and sum(weights)+cur <= weight:
            times.append(0)
            weights.append(cur)
            cur = next(truck, False)
        
        return answer


##--------------------------------------------------------------------------##
#class의 활용

import collections

DUMMY_TRUCK = 0

class Bridge(object):
    def __init__(self, lenght, weight):



bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
