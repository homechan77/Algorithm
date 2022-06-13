k, n = map(int, input().split())
klist = [int(input()) for _ in range(k)]

# # 시간 초과
# def solution(n, klist):
#     answer = 1
#     while True:
#         tmp = 0
#         for i in klist:
#             mok = i // answer
#             tmp += mok
#         if tmp < n:
#             return answer-1
#         answer += 1


# # 이진 탐색(반복)
# def solution2(n, klist):
#     start = 1
#     end = max(klist)
#     while start <= end:
#         mid = (start + end) // 2

#         tmp = 0
#         for i in klist:
#             tmp += i // mid
            
#         if n <= tmp:
#             start = mid + 1
#         else:
#             end = mid - 1

#     return end


# 이진 탐색(재귀)
start = 1
end = max(klist)

def solution3(n, klist):
    global start, end
    # start = 1
    # end = max(klist)
    mid = (start+end)//2
    if start > end:
        return end
    
    tmp=0
    for i in klist:
        tmp += i//mid
    
    if tmp >= n:
        start = mid+1
        return solution3(n, klist)
    else:
        end = mid-1
        return solution3(n, klist)
    
print(solution3(n, klist))