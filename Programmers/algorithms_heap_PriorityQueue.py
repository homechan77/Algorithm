##--------------------------------------------------------------------------##
# 최대 힙
# import heapq

# nums = [4, 1, 7, 3, 8, 5]
# heap = []

# for num in nums:
#   heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

# while heap:
#   print(heapq.heappop(heap)[1])  # index 1
##--------------------------------------------------------------------------##
  
  
##--------------------------------------------------------------------------##  
# 1. 내가 작성한 코드: "IndexError: index out of range" 오류 발생
# import heapq

# def solution(operation):
#     answer = []
#     maxheap = []
#     minheap = []
    
#     for i in operation:
#         isplit = i.split()
#         num = int(isplit[1])

#         if isplit[0] == 'I':
#             heapq.heappush(minheap, num)
#             heapq.heappush(maxheap, (-num, num))
#             answer.append(num)
        
#         # 최대값 삭제
#         elif isplit[0] == 'D' and num > 0:
#             ma = heapq.heappop(maxheap)[1]
#             minheap.remove(ma)
#             answer.remove(ma)
            
#         # 최소값 삭제
#         elif isplit[0] == 'D' and num < 0:
#             mi = heapq.heappop(minheap)
#             # minus_mi = -mi
#             maxheap.remove((-mi, mi))
#             answer.remove(mi)
    
#     if len(answer) == 0:
#         return [0,0]
#     else:
#         fi_answer = sorted(answer)
#         # # fi_min = fi_answer[0]
#         # # fi_max = list(reversed(fi_answer))[0]
#         # return [fi_max, fi_min]
#         return [max(fi_answer), min(fi_answer)]

# operation = ["I 7","I 5","I -5","D -1"]		
# print(solution(operation))
##--------------------------------------------------------------------------##
import heapq
def solution(operations):
    heap = []
    max_heap = []
    
    for o in operations:
        osplit = o.split()
        if osplit[0] == 'I':
            num = int(osplit[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num*-1, num))
        else:
            # 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
            if len(heap) == 0:
                pass
            elif osplit[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif osplit[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value*-1, min_value))
                
    # 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0,0]
    
operations = ["I 7","I 5","I -5","D -1"]		
print(solution(operations))