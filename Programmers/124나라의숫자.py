"""
def solution(n):
    if n==1 or n==2:
        return str(n)
    elif n==3:
        return str(4)
    
    result = []
    while n>0:
        if n%3==0:
            tmp = n%2
            if tmp == 3:
                result.append(4)
            else:
                result.append(tmp)
            n = n//2
        else:
            result.append(n%3)
            n = n//3
    answer = "".join(map(lambda x: str(x), sorted(result, reverse=True)))
    return answer
"""
# 참고) https://hoons-dev.tistory.com/67

def solution(n):
    result = []
    while n:
        t = n%3
        # t가 0인 경우(n이 3의 배수인 경우)           
        if not t:
            t = 4
            n -= 1
        result.append(str(t))
        n //= 3
    answer = "".join(result[::-1])
    return answer