# deque()를 활용한 문제풀이
from collections import deque


def solution(priorities, location):
    listx = []
    # priorites 리스트 안 원소들을 enumerate() 함수를 활용하여 인덱스와 원소로 이루어진 튜플(entry)로 생성 후 listx 리스트 안에 넣어준다.(value값이 index보다 앞으로 나오게 [::-1]을 추가했다.)
    # 이후 list를 deque로 변환한다.
    for entry in enumerate(priorities):
        listx.append(entry[::-1])
    deq = deque(listx)

    count = 0
    
    # deq내의 모든 원소들이 사라질 때까지 계속해서 반복문을 진행한다.
    while deq:
        # deq의 첫번째를 원소를 deq 전체의 최대값과 비교 후 최대값이 맞을 경우 해당 원소를 지워버림과 동시에 count를 1씩 증가시킨다.
        # 만약 최대값이 아니라면 deque()의 rotate(-1)함수를 활용하여 왼쪽으로 1칸씩 밀어낸다.(맨 왼쪽의 원소는 맨 오른쪽으로 이동)
        # 최대값이어서 지워버릴 때 해당 튜플의 인덱스가 location 객체의 값과 일치할 경우 반복문을 중단하고 빠져나와 count를 반환한다.
        # 튜플들간의 크기 비교에 있어서 튜플내의 첫번째 요소를 비교한 후 같은 경우 그 다음 번째 요소를 비교하며 최종적인 크기 비교를 진행한다. 따라서 반복문을 진행 중에 모든 튜플의 첫번째 요소가 같은 경우 차례차례 지워나가야 하지만 튜플 비교 원칙에 따라 그 다음 요소를 비교하는 경우가 생기므로 (Ex.(1,2)>(1,1)) "or deq[0][0] == max(deq)[0]" 코드를 삽입하여 해당 경우를 미연에 방지하였다.
        if deq[0] == max(deq) or deq[0][0] == max(deq)[0]:
            temp = deq.popleft()
            count += 1
            if temp[1] == location:
                break
        elif deq[0] != max(deq):
            deq.rotate(-1)

    return count


priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))