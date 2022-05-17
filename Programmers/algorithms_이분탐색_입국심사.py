# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return

def solution(n, times):
    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = 0
        for t in times:
            count += mid//t
            # if count >= n:
            #     break
        
        if count >= n:
            answer = mid
            right = mid-1
        elif count < n:
            left = mid+1
    
    return answer
    
"""
# 실패
    timemin = min(times)
    timemax = max(times)*n
    
    # timelist = [i for i in range(timemin, timemax+1)]

    def binary_search(target, start, end):
        mid = (start + end) // 2
        
        x = sum([mid//i for i in times])
        remain = [mid%j for j in times]
            
        if x == target:
            if 0 not in remain:
                return binary_search(target, start, mid+1)
            return mid
        elif x > target:
            return binary_search(target, start, mid-1)
        else:
            return binary_search(target, mid+1, end)
    
    answer = binary_search(n, timemin, timemax)
    
    return answer
"""

n = 6
times = [7, 10]
print(solution(n, times))
# return: 28