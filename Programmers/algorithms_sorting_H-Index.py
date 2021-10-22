def solution(citations):
    # https://www.ibric.org/myboard/read.php?Board=news&id=270333 (문제 이해가 전부인 문제)
    citations.sort(reverse=True)
    listx = [i for i in range(len(citations))]
    
    for i, j in zip(citations, listx):
        if i <= j:
            answer = j
            break
    
    # 테스트케이스가 [9,9,9,12]와 같은 경우 반복문 중 조건문에 해당하는 경우가 없으므로 반복문을 빠져나오지 못한다.<br> 따라서 for-else 구문을 활용하여 반복문 수행 종료시 반환 대상 객체 answer가 다음과 같은 값을 갖도록 한다. 
    else:
        answer = len(listx)
        
    return answer