# 소수란 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수다. 예를 들어, 5는 1×5 또는 5×1로 수를 곱한 결과를 적는 유일한 방법이 그 수 자신을 포함하기 때문에 5는 소수이다. 그러나 6은 자신보다 작은 두 숫자의 곱(2×3)이므로 소수가 아닌데, 이렇듯 1보다 큰 자연수 중 소수가 아닌 것은 합성수라고 한다.

from itertools import permutations

def solution(numbers):
    nslist = list(numbers)
    
    # 주어진 numbers에 대한 "순열(permutation)" 계산
    result = []
    for i in range(len(nslist)):
        permu = list(permutations(nslist, i+1))
        for j in range(len(permu)):
            toint = int(''.join(permu[j]))
            # 순열 계산 값이 0,1일 경우 순열 결과값들의 리스트 result에 저장 안함
            if toint <= 1:
                continue
            # 순열값이 0,1이 아닌 가운데 result가 비워져 있을 경우 해당 값을 result에 저장
            elif len(result) == 0:
                result.append(toint)
                continue
            # 중복되는 순열값을 제거하기 위하여 result 안에 해당되는 값이 있는지 확인
            # 중복되는 순열값이 없을 경우 ValueError가 발생한다에 착안, 오류를 발생시키는 값을 result에 저장
            try:
                result.index(toint)
            except ValueError:
                result.append(toint)
    
    # 소수 판별 함수를 통해서 최종값 도출
    answer = []
    for k in result:
        if is_prime_number(k) == True:
            answer.append(k)
    
    return len(answer)
                

# 소수 판별 함수: 주어진 x에 대하여 2부터 x-1의 값을 나누어 준다. 만약에 하나라도 나누어 떨어지면 해당 함수는 소수가 아니므로 탈락
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

numbers = "17"
print(solution(numbers))