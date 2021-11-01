import math

def solution(progresses, speeds):
    # 작업 기간 계산 후 wd 리스트에 저장한다.
    # 실수 형태의 결과들을 math.ceil 함수를 활용하여 올림한다.
    wd = []
    for i in range(len(progresses)):
        x = math.ceil((100 - progresses[i]) / speeds[i])
        wd.append(x)


    # 몇개의 기능이 배포될지 count한 후 answer 리스트에 저장한다.
    # "while wd:"를 활용하여 wd 리스트 내의 모든 원소들이 없어질 때 까지 반복한다. 
    count = 0
    answer = []
    
    while wd:
        # 첫 원소의 경우 해당 값을 pop() 함수를 활용하여 객체(removed)로 저장 후 삭제 처리한다.
        if len(wd) == len(progresses):
            removed = wd.pop(0)
            count += 1

        # 리스트의 맨 처음 원소들을 기준으로 해당 원소들이 앞서 저장한 removed의 값보다 크거나 작은 경우를 나누어 계산한다.
        # 큰 경우 앞서 계산되어진 count 값을 answer 리스트에 저장하고 count 값을 0으로 초기화한다.
        # 이후 자신을 removed로 지정하고 초기화되어진 count 값을 올려준다.
        if removed < wd[0]:
            answer.append(count)
            count = 0

            removed = wd.pop(0)
            count += 1
        
        else:
            wd.pop(0)
            count += 1

        # 리스트 내의 원소가 더 이상 없을 경우 마지막으로 저장한 count 값을 answer 리스트에 저장한다.
        if len(wd) == 0:
            answer.append(count)


    return answer

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))