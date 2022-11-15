# DP
def solution(land):
    dp = []
    dp.append(land[0])
    for i in range(1, len(land)):
        result = []
        for j, x in enumerate(land[i]):
            tmp = []
            for k in range(4):
                if k == j:
                    continue
                tmp.append(dp[i-1][k])
            maxn = max(tmp)
            result.append(maxn+x)
        dp.append(result)
    return max(dp[-1])
