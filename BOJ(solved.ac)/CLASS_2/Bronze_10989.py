import sys

n = int(sys.stdin.readline())

# # 시도1. 메모리 초과
# nlist = sorted([int(sys.stdin.readline()) for _ in range(n)])
# for i in nlist:
#     print(i)
##--------------------------------------------------------------------------##  

# 시도2. 정답자 코드 참고_계수 정렬
# 계수 정렬은 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용할 수 있다.
# 계수 정렬은 데이터 크기가 제한되어 있을 때에 한해서 데이터의 개수가 매우 많더라도 빠르게 동작한다.

def solution(n):
    nlist = [0]*10001
    for i in range(n):
        nlist[int(sys.stdin.readline())] += 1

    for j in range(len(nlist)):
        for _ in range(nlist[j]):
            print(j)

solution(n)
        
