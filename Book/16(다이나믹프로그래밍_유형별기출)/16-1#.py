# 금광

import sys

input = sys.stdin.readline

t = int(input())

def make_mine_graph(n, m, input_mine):
    minegraph = [[] for _ in range(n)]
    for i, x in enumerate(input_mine):
        indexing = i // m
        minegraph[indexing].append(x)
    return minegraph

def dp_work(n, m , mine, dp):
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1]+mine[i][j], dp[i+1][j-1]+mine[i][j])
            elif i == n-1:
                dp[i][j] = max(dp[i-1][j-1]+mine[i][j], dp[i][j-1]+mine[i][j])
            else:
                dp[i][j] = max(dp[i-1][j-1]+mine[i][j], dp[i][j-1]+mine[i][j], dp[i+1][j-1]+mine[i][j])
    
    maxanswer = 0
    for k in range(n):
        if dp[k][m-1] > maxanswer:
            maxanswer = dp[k][m-1]
        
    return maxanswer
                
def solution(input, t):
    for _ in range(t):
        n, m = map(int, input().split())
        inputmine = list(map(int, input().split()))
        mine = make_mine_graph(n, m, inputmine)        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = mine[i][0]
        answer = dp_work(n, m, mine, dp)
        print(answer)
        
solution(input, t)