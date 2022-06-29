# M이상 N이하의 소수를 모두 출력

# # 시간 초과(에스토스테네스 방식 구현)
# import time
# from collections import deque

# start = time.time()

# m,n = map(int, input().split())

# def solution(m, n):
#     nlist = [i for i in range(2, n+1)]
#     queue = deque(nlist)
#     while queue:
#         pop = queue.popleft()
#         if pop >= m:
#             print(pop)
#         tmp = 2
#         popcopy = 0
#         while popcopy <= n:
#             popcopy = pop*tmp
#             tmp += 1
#             try: 
#                 queue.remove(popcopy)
#             except ValueError:
#                 continue

# solution(m, n)

# end = time.time()
# print(end-start)

##--------------------------------------------------------------------------##
# 제곱근 값(루트 값)을 기준으로 앞에 있는 수들만을 검사해 시간 초과 방지
import math

m, n = map(int, input().split())

def solution2(m, n):
    for i in range(m, n+1):
        if i==0 or i==1:
            continue
        
        cnt = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                break
            cnt += 1
        
        if cnt == int(math.sqrt(i))-1:
            print(i)

solution2(m, n)