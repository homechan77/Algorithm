# 완주하지 못한 선수

# 시도1
# 효율성 테스트 실패(시간초과)

def solution(participant, completion):
    
    for i in completion:
        for j in participant:
            if i == j:
                participant.remove(j)
                break
    
    answer = participant[0]
    
    return answer
##--------------------------------------------------------------------------##

# 시도2
# participant와 completion을 정렬 후 쌍 비교

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] != completion[i]:



    return 



participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))