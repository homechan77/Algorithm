from collections import Counter

def solution(str1, str2):
    # 알파벳 대문자 아스키 코드 값들 리스트
    alpha = [k for k in range(65, 91)]

    # 두글자씩 끊어서 다중집합 생성, 알파벳 이외의 문자가 삽입된 경우 제외(아스키 코드로 알파벳인지 판별)
    strlist = [str1, str2]
    strcombi = [[] for _ in range(2)]
    for i in range(len(strlist)):
        strlist[i] = strlist[i].upper()
        for j in range(len(strlist[i])-1):
            if ord(strlist[i][j]) in alpha and ord(strlist[i][j+1]) in alpha:
                strcombi[i].append((strlist[i][j], strlist[i][j+1]))

    # 다중집합 내의 원소 값들의 갯수 계산(원소(key)-갯수(value) 딕셔너리)
    str1info = Counter(strcombi[0])
    str2info = Counter(strcombi[1])

    # 키 값인 원소 값만 추출 후 교집합, 합집합 처리
    str1key = list(str1info.keys())
    str2key = list(str2info.keys())

    gyolist = list(set(str1key).intersection(set(str2key)))
    haplist = list(set(str1key).union(set(str2key)))

    # 집합 A와 집합 B가 모두 공집합일 경우 J(A, B) = 1로 정의한다는 예외 설정
    if len(str1info)==0 and len(str2info)==0:
        return 65536
    
    # 자카드 유사도 계산
    gyo = 0
    for x in gyolist:
        gyo += min(str1info[x], str2info[x])
    
    hap = 0
    for y in haplist:
        if y in str1key and y in str2key:
            hap += max(str1info[y], str2info[y])
        elif y in str1key:
            hap += str1info[y]
        else:
            hap += str2info[y]

    answer = int((gyo / hap) * 65536)

    return answer


str1 = 'FRANCE'
str2 = 'french'
# str1 = 'A+C'
# str2 = 'DEF'
# result: 0
print(solution(str1, str2))