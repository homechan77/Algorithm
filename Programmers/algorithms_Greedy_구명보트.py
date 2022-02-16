# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 
# 한 번에 최대 2명씩 밖에 탈 수 없고

'''
# 시도1 - 실패
def solution(people, limit):
    people.sort(reverse=True)
    answer = []
    while people:
        popn = people.pop(0)
        remainb = limit - popn
        templist = []
        templist.append(popn)
        
        while remainb > 0:
            people.reverse()
            
            if not people:
                break
            
            elif len(templist) >= 2:
                break
            
            elif people[0] > remainb:
                remainb -= people[0]
                continue
            else:
                withb = people.pop(0)
                templist.append(withb)
                remainb -= withb
                
        people.reverse()
        answer.append(templist)
            
    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))
'''
# 시도2 - 성공
# tip1. 효율성 테스트를 통과하려면 반복문을 1번만 사용해야 한다.
# tip2. pop() 함수를 사용하게 될 경우도 효율성 테스트에서 걸린다.

from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = []
    while people:
        popn = people.pop()
        if not people:
            answer.append([popn])
            break
        elif popn + people[0] <= limit:
            answer.append([people.popleft(), popn])
        else:
            answer.append([popn])
            
    return len(answer)
    
people = [70, 80, 50]
limit = 100
print(solution(people, limit))
