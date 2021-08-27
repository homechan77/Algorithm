#코딩테스트 연습_2021 KAKAO BLIND RECRUITMENT

    #1단계
    new_id = list(new_id.lower())

    #2단계
    refined = []
    for i in new_id:
        if i.isalpha() == True:
            refined.append(i)
        elif i.isdigit() == True:
            refined.append(i)
        elif i in ['-', '_', '.']:
            refined.append(i)

    #3단계
    list3 = []
    for i in range(len(refined)):
        if refined[i] in ['.']:
            list3.append(i)
    
    delli = []
    for j in range(len(list3)):
        if j == 0:
            continue
        if list3[j] - list3[j-1] == 1:
            delli.append(j)

    for k in range(len(delli)):
        if k != 0:
            list3[delli[k]] -= k
        del refined[list3[delli[k]]]

    #4단계
    if refined[0] in ['.']:
        del refined[0]
    elif refined[len(refined)-1] in ['.']:
        del refined[len(refined)-1]

    #5단계
    if len(refined) == 0:
        refined.append('a')

    #6단계
    if len(refined) >= 16:
        del refined[15:]
    if refined[len(refined)-1] in ['.']:
        del refined[len(refined)-1]

    #7단계
    if len(refined) <= 2:
        while len(refined) < 3:
            refined.append(refined[len(refined)-1])

    #result
    answer = ''.join(refined)
    return answer

### 1. 객체명, 반복문 개체 일관되게 정리하면서 코딩하기.
### 2. 실력을 쌓으면서 점점 간결하면서도 깔끔한 코드를 짜려고 노력하기.
### 3. 고수들은 정규식으로 푼다.