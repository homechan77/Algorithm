# 유클리드 호제법을 이용한 최대공약수 계산
# 참고) https://velog.io/@yerin4847/W1-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95
# n과 m의 곱을 최대공약수로 나누어 주면 최소공배수
n, m = map(int, input().split())

def solution(n, m):
    ncopy, mcopy = n, m
    if n < m:
        n,m = m,n
    while m > 0:
        n, m = m, n%m
    gcd = n
    print(gcd)
    lcm = (ncopy*mcopy)//gcd
    print(lcm)

solution(n, m)