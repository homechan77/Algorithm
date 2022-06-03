# 윈도우 스캔 방식
# 정확성: 테스트8, 14번 실패, 효율성: 모두 시간 최과
# 3중 반복문만 사용해도 시간초과
# 파이썬이 1초에 가능한 연산수 약 2천만(알고리즘 문제의 대부분은 제한시간은 2~3초)
def solution(board):
    rown = len(board)
    coln = len(board[0])
    scanwindow = min(rown, coln)
    while True:
        for k in range(scanwindow, 0, -1):
            for i in range(rown-(k-1)):
                for j in range(coln-(k-1)):
                    tmp = []
                    a = []
                    for x in range(k):
                        tmpa = []
                        for y in range(k):
                            tmpa.append(board[i+x][j+y])
                        a.append(tmpa)
                    [tmp.extend(l) for l in a] 
                    if len(set(tmp)) == 1:
                        return k*k

##--------------------------------------------------------------------------##

# DP(Dynamic Programming)를 활용
def solution2(board):
    rown = len(board)
    coln = len(board[0])
    
    # dp 테이블 세팅
    dp = [[0]*coln for _ in range(rown)]
    for i in range(rown):
        if i == 0:
            dp[i] = board[i]
        else:
            dp[i][0] = board[i][0]
    
    # answer = 1
    
    # 반복문(bottom-up) 방식의 dp 실행
    for x in range(1, rown):
        for y in range(1, coln):
            if board[x][y] == 1:
                minn = min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1]) + 1
                dp[x][y] = minn
                # if minn > answer:
                #     answer = minn
    
    answer = max([max(l) for l in dp])
                
    return answer**2
    

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution2(board))