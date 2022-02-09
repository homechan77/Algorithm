# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬
# 1번 수포자: 1, 2, 3, 4, 5
# 2번 수포자: 2, 1, 2, 3, 2, 4, 2, 5
# 3번 수포자: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
def solution(answers):
    cycling = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    relist = []
    lenanswers = len(answers)
    
    # 정답 개수를 통해 수포자들이 제출한 문제 개수를 재조정
    for i in range(len(cycling)):
        mok = lenanswers // len(cycling[i]) 
        namuji = lenanswers % len(cycling[i])
        
        if mok > 0:
            relist.append(cycling[i] * mok)
            for j in range(namuji):
                relist[i].append(cycling[i][j])
        else:
            relist.append([])
            for k in range(namuji):
                relist[i].append(cycling[i][k])
    
    # 수포자들의 점수 산출
    result = []         
    count = 0
    for l in relist:
        for m in range(lenanswers):
            if l[m] == answers[m]:
                count += 1
            if m == lenanswers-1:
              result.append(count)
              count = 0  
    
    # 가장 높은 점수의 수포자를 반환, 가장 높은 점수를 받은 사람이 여럿일 경우 return하는 값을 오름차순 정렬
    final_result = []
    maxresult = max(result)
    for n in range(len(result)):
        if result[n] == maxresult:
            final_result.append(n+1)
        
    return final_result

answers = [1,3,2,4,2]
print(solution(answers))



