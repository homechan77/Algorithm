#코딩테스트 연습_2021 KAKAO BLIND RECRUITMENT_순위 검색

"""
## 1. 첫번째 시도 소스코드 - 실패(런타임 오류)
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



## 2. 리스트 컴프리헨션 방법 사용 및 반복문에서 break을 사용하여 실행 시간 단축 유도 - 실패(런타임 오류, 실행시간 초과)
def solution(info, query):
    
    # info split
    new_info = [x.split() for x in info]

    #예를 들면, "cpp and - and senior and pizza 500"은 "cpp로 코딩테스트를 봤으며, 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람은 모두 몇 명인가?"를 의미합니다.
    # query split / 'and' 삭제
    temp_query = [y.split() for y in query] #query split
    new_query = [[x for x in query_list if x != 'and'] for query_list in temp_query] #remove 'and'
    
    answer = [0] * len(new_info)
    
    # 조건에 대한 정보 일치 여부 판별
    for i in new_query:
        for j in new_info:
            count = 0
            for k in range(4):
                if j[k] == i[k] or i[k] in '-':
                    count += 1
                else:
                    break

            if count == 4 and int(j[4]) >= int(i[4]):
                answer[new_query.index(i)] += 1
                           
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))
"""

## 3. 이진 탐색을 활용한 풀이 방법

def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-',]:
        for b in ['backend', 'frontend', '-']:
            for c in ['senior', 'junior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a,b,c,d), list())
    

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a,b,c,d)].append(int(i[4]))
    
    
    return data = 150
    
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))


