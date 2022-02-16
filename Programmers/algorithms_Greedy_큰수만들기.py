"""
# 시간초과 발생 - combination(조합) 사용
from itertools import combinations

def solution(number, k):
    p = len(number) - k
    
    combinationlist = list(combinations(number, p))
    
    answer = []
    for i in combinationlist:
        answer.append(int(''.join(i)))
    
    
    return str(max(answer))

number = "4177252841"
k = 4
print(solution(number, k))
"""

# 해설 참조(1) - stack(LIFO) 활용
def solution(number, k):
    stack = []
    leng = len(number) - k
    for n in number:
        # 3가지의 조건을 모두 만족할 경우 해당 while 반복문을 수행: (1)stack에 원소가 존재하며 (2)k가 0보다 크고 (3)push할 n이 기존 stack의 마지막 자리 수보다 클 경우
        # (문제... k개를 제거를 제거할 경우)
        while stack and k>0 and stack[-1]<n:
            stack.pop()
            k -= 1
        stack.append(n)
    
    return ''.join(stack[:leng])

number = "1231234"	
k = 3
print(solution(number, k))
                        
# # 해설 참조(2)
# def solution(number, k):
#     answer = []
    
#     for n in number:
#         if not answer:
#             answer.append(n)
#             continue
#         if k>0:
#             while answer[-1] < n:
#                 answer.pop()
#                 k -= 1
#                 if not answer or k <= 0:
#                     break
#         answer.append(num)
        
#     answer = answer[:-k] if k>0 else answer
#     return ''.join(answer)
    
# number = "1924"
# k = 2
# print(solution(number, k))   