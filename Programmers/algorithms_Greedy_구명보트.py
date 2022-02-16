# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 
# 한 번에 최대 2명씩 밖에 탈 수 없고...


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
            
            
    return len(answer)

people = [160, 150, 140, 60, 50, 40]
limit = 200
print(solution(people, limit))