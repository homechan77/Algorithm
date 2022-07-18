# 외벽 점검
# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
        
    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + friends[cnt-1]
            for index in range(start+1, start+length): # for index in range(1, length):
                if position < weak[index]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[index] + friends[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer
                

n = 12 # 외벽의 길이
weak = [1, 5, 6, 10] # 취약 지점의 위치가 담긴 배열
dist = [1, 2, 3, 4]	# 각 친구가 1시간 동안 이동할 수 있는 거리
print(solution(n, weak, dist))
