# 체육수업을 들을 수 있는 학생의 최댓값을 return

def solution(n, lost, reserve):
    # 전체 학생 수(n)에 대해서 각 학생들은 체육복을 가지고 있을 것이라는 가정 하에 리스트 생성 
    alist = [1] * n
        
    # 체육복이 없는 학생들에게 -1
    for j in lost:
        alist[j-1] -= 1
    
    # 여별의 체육복을 가지고 있는 학생들에게 +1
    for i in reserve:
        alist[i-1] += 1
     
    # 체육복이 없는 학생(0)이 인접한 다른 학생들을 비교하면서 체육복을 빌릴 수 있는지 확인
    # 좌측 우선 비교
    for k in range(len(alist)):
        if alist[k] == 0:
            # 첫번째 학생이 체육복이 없는 경우(0) 좌측 비교 skip
            if k != 0 and alist[k-1] == 2:
                alist[k] += 1
                alist[k-1] -= 1
                continue
            # 마지막 학생은 우측 비교 skip
            if k+1 == n:
                continue
            elif alist[k+1] == 2:
                alist[k] += 1
                alist[k+1] -= 1
                
    # 체육복을 가진 학생(0이상의 값을 가지는) 카운트
    answer = 0 
    for k in alist:
        if k != 0:
            answer += 1

    return answer

n = 4
lost = [3,1]
reserve = [2,4]
print(solution(n, lost, reserve))



