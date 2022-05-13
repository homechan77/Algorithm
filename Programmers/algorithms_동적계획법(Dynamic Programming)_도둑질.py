# 참고: https://aliwo.github.io/swblog/python3/algorithm/thievery/#
# dp[i] = max(dp[i-2]+money[i], dp[i-1])

def solution(money):
    cache = [money[0], money[0]]
    cache2 = [0, money[1]]
    
    for i in range(2, len(money)-1):
        cache.append(max(cache[i-2]+money[i], cache[i-1]))
        
    for j in range(2, len(money)):
        cache2.append(max(cache2[j-2]+money[j], cache2[j-1]))
    
    return max(cache[-1], cache2[-1])

money = [1000,0,0,1000,0,0,1000,0,0,1000]
print(solution(money))

# return: 4
