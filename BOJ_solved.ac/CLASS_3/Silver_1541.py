# 잃어버린 괄호
# 최솟값을 만들기 위해서는 - 기준으로 괄호를 치면 된다.
# 예를 들어 55 - 50 + 40 - 30 + 20 위와 같이 입력을 받았을때 - 기준으로 55 - (50 + 40) - (30 + 20) 이렇게 괄호를 쳤을때 최솟값이 된다.

import sys

input = sys.stdin.readline
exp = input()

def solution(exp):
    memory = 0
    forsum = []
    result = []
    for i in range(len(exp)):
        if exp[i] == '+' or exp[i] == '-' or i == len(exp)-1:
            forsum.append(int(exp[memory:i]))
            memory = i+1
            if exp[i] == '-':
                result.append(sum(forsum))
                forsum = []
    if len(forsum) != 0:
        result.append(sum(forsum))
    
    answer = 0
    for i in range(len(result)):
        if i == 0:
            answer = result[i]
            continue
        answer -= result[i]

    return answer

print(solution(exp))