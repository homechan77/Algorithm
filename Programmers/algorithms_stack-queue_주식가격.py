from collections import deque

# 효율성 테스트 실패
# def solution(prices):
#     answer = []
#     queue = deque(prices)
#     while queue:
#         pop = queue.popleft()
#         if len(answer) == 0:
#             answer.append([pop, 1])
#             continue
#         if len(queue) == 0:
#             answer.append([pop,0])
#             break
#             # return list(map(lambda x: x[1], answer))
#         for i in answer:
#             if i[0] <= pop:
#                 i[1] += 1
#             else:
#                 i[0] = int(1e4)+1
#         answer.append([pop,1])
    
#     answer_list = list(map(lambda x: x[1], answer))
    
#     return answer_list

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        pop = queue.popleft()
        count = 0 
        for i in queue:
            count += 1
            if pop > i:
                break
        answer.append(count)
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))	
# return: [4, 3, 1, 1, 0]