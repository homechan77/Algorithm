# bfs 활용-실패
# from collections import deque

# def bfs(n):
#     queue = deque([1, 2])
#     cnt = 0
#     while queue:
#         pop = queue.popleft()
#         if pop == n:
#             cnt += 1
#         if pop+1 <= n:
#             queue.append(pop+1)
#         if pop+2 <= n:
#             queue.append(pop+2)
#     return cnt

# def solution(n):
#     answer = bfs(n)
#     return answer

##--------------------------------------------------------------------------##
# DP
def solution(n):
    if n in ([1, 2]):
        return n%1234567
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n]%1234567
    return answer