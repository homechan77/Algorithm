# 스티커 모으기(2)
'''
# dfs 활용-실패
import copy

answer = 0
visited = []

def dfs(sticker, result):
    global answer
    
    stickercopy = copy.deepcopy(sticker)
    for i in range(len(stickercopy)):
        n = stickercopy[i]
        tmpresult = result
        start, end = i-1, i+1
        if len(stickercopy) < 3:
            tmpresult += n
            if tmpresult > answer:
                answer = tmpresult
            continue
        if end == len(stickercopy):
            del stickercopy[start:]; del stickercopy[0]
        elif start < 0:
            del stickercopy[-1]; del stickercopy[:end+1]
        else:
            del stickercopy[start:end+1]
        tmpresult += n
        if len(stickercopy) != 0:
            if stickercopy not in (visited):
                visited.append(stickercopy)
                dfs(stickercopy, tmpresult)
        else:
            if tmpresult > answer:
                answer = tmpresult
        stickercopy = copy.deepcopy(sticker)
    return

def solution(sticker):    
    global answer

    dfs(sticker, 0)
    return answer

sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))
'''
# dp 활용
# 참조) https://latte-is-horse.tistory.com/231

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    dp1, dp2 = [0]*len(sticker), [0]*len(sticker)
    # dp1 - 맨 앞을 뜯은 경우
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, len(sticker)-1):
        dp1[i] = max(sticker[i]+dp1[i-2], dp1[i-1])
    # dp2 - 맨 앞을 뜯지 않은 경우
    for i in range(1, len(sticker)):
        dp2[i] = max(sticker[i]+dp2[i-2], dp2[i-1])
    
    return max(dp1[-2], dp2[-1])

sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))