"""
## 첫번째 시도 소스코드
def solution(info, query):
    answer = [0]*6
    
    # info split
    new_info = []
    for i in info:
        new_info.append(i.split())

    # query split / 'and' 삭제
    temp1 = []
    for i in query:
        temp1.append(i.split())
    
    new_query = []
    for j in temp1:
        temp2 = [x for x in j if x != 'and']
        new_query.append(temp2)
    
    # 조건에 대한 정보 일치 여부 판별
    for i in new_query:
        for j in new_info:
            count = 0
            for k in range(len(j)):
                if k < 4:
                    if j[k] == i[k] or i[k] in '-':
                        count += 1
                else:
                    if int(j[k]) >= int(i[k]) or i[k] in '-':
                        count += 1
            if count == len(j):
                answer[new_query.index(i)] += 1 
                           
    return answer
"""


## 리스트 컴프리헨션 방법 사용 및 반복문에서 break을 사용하여 실행 시간 단축 유도
def solution(info, query):
    
    # info split
    new_info = [x.split() for x in info]

    # query split / 'and' 삭제
    temp_query = [y.split() for y in query] #query split
    new_query = [[x for x in query_list if x != 'and'] for query_list in temp_query] #remove 'and'
    
    answer = [0] * len(new_info)
    
    # 조건에 대한 정보 일치 여부 판별
    for i in new_query:
        for j in new_info:
            count = 0
            for k in range(len(j)):
                if k < 4:
                    if j[k] == i[k] or i[k] in '-':
                        count += 1
                    else:
                        break
                else:
                    if int(j[k]) >= int(i[k]) or i[k] in '-':
                        count += 1

            if count == len(j):
                answer[new_query.index(i)] += 1 
                           
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))


## DFS/이진탐색 알고리즘을 활용한 코드 작성
