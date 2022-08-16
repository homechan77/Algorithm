n = int(input())

# 메모리 초과
def solution(n):
    answerlist = [[1]]
    start = 2
    interval = 6
    while True:
        tmp = []
        for i in range(2, start+interval):
            tmp.append(i)
            if i == n:
                answerlist.append(tmp)
                return len(answerlist)
        answerlist.append(tmp)
        start += interval
        interval += 6
        
# print(solution(n))
##--------------------------------------------------------------------------##
# 메모리 초과 문제를 해결하기 위해서 배열 미사용_성공
def solution2(n):
    start = 2
    interval = 6
    cnt = 1
    if n==1:
        return cnt
    while True:
        if n < start+interval:
            cnt+=1
            return cnt
        start += interval
        interval += 6
        cnt+=1
        
print(solution2(n))



