from collections import deque

def solution(s):
    cnt = 1
    answer = 0
    
    # 1부터 문자열 s의 길이 값까지 s를 쪼개는 경우를 반복하고 문자열을 압축하여 가장 길이가 짧은 값을 answer 변수에 갱신
    while cnt <= len(s):
        # cnt 값을 기준으로 문자열 s를 쪼개고 tmp 리스트에 저장
        tmp = []
        x=0
        if len(s)%cnt > 0:
            iter = (len(s)//cnt)+1
        else:
            iter = (len(s)//cnt)
            
        for i in range(iter):
            if i== iter-1:
                tmp.append(s[x:])
            else:
                tmp.append(s[x:x+cnt])
            x = x+cnt
        
        # tmp 리스트 왼쪽부터 하나씩 꺼내어 문자열 압축 표현
        tmp2 = []
        queue = deque(tmp)
        while queue:
            pop = queue.popleft()
            if len(tmp2)==0 or tmp2[-1][0] != pop:
                tmp2.append([pop, 1])
            else:
                tmp2[-1][1] += 1
        
        # 문자열 압축 표현 길이 계산
        tmpanswer = 0
        for i in tmp2:
            if i[1] != 1:
                tmpanswer += len(i[0])+len(str(i[1]))
            else:
                tmpanswer += len(i[0])
        
        # 계산된 tmpanswer 값이 앞선 반복문의 tmpanswer 값보다 작은 경우 기존 answer 값을 갱신
        if cnt==1 or tmpanswer < answer:
            answer = tmpanswer
        
        cnt += 1
        
    return answer


s = "abcabcabcabcdededededede"	
print(solution(s))