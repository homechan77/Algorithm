from collections import Counter

def solution(N, stages):
    nstage = len(stages)
    cstage = Counter(stages)
    result = []
    for i in range(N):
        i += 1
        if cstage[i] == 0:
            result.append((i, 0))
        else:
            result.append((i, cstage[i]/nstage))
        nstage -= cstage[i]
    result.sort(key = lambda x: ([-x[1], x[0]]))
    answer = list(map(lambda x: x[0], result))
    return answer

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))