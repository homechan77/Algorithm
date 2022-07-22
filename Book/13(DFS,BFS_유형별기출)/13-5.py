'''
문제에서 "주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 
총 60가지의 식을 만들 수 있다."라고 했는데, 그렇다면 5!로, 5x4x3x2x1 = 120 가지가 나와야 하는데 
왜 60가지지..? 라는 의문을 가졌었다.
혹시나 하고 질문 리스트를 확인해본 결과"덧셈 2개는 구분할 수 없으므로 2로 나눠줘야 합니다." 
라는 글이 있었다...
'''
# 연산자 끼워넣기
# 중복 순열 product "from itertools import product"

import sys
from itertools import permutations, product
from collections import deque

input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
operatorn = list(map(int, input().split()))

def solution(n, nlist, operatorn):
    operator = ['+', '-', '*', '//']
    tmp = []
    for i in range(len(operatorn)):
        for _ in range(operatorn[i]):
            tmp.append(operator[i])
    pertmp = list(set(permutations(tmp, n-1)))
    
    result = []
    # 음수를 양수로 나눌 때 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
    for i in pertmp:
        queue = deque(i)
        for j in range(len(nlist)):
            if j == 0:
                a = nlist[j]
                continue
            while queue:
                pop = queue.popleft()
                if pop == '+':
                    a += nlist[j]
                    break
                elif pop == '-':
                    a -= nlist[j]
                    break
                elif pop == '*':
                    a *= nlist[j]
                    break
                else:
                    if a < 0:
                        a *= -1
                        a = a // nlist[j]
                        a *= -1
                        break
                    else:
                        a = a // nlist[j]
                        break
        result.append(a)
    
    print(max(result), min(result), sep='\n')
                
solution(n, nlist, operatorn)