import itertools

def solution(clothes):
    closet = {}
    answer = 1

    #기존 2차원 형태의 리스트를 딕셔너리 형태로 변경
    for cloth in clothes:
        #중복되는 key값에 value값 추가하기(<- 때문에 딕셔너리 내의 value 값을 저장할 때 리스트 형태로 저장... appennd()함수 사용 가능)
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
    
    #경우의 수 계산
    #
    for value in closet.values():
        answer *= len(value) + 1

    return answer-1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))

'''
예시로 d = [“A”: [“a”, “b”] , “B”: [“c”, “d”]]
(A, B 종류의 옷이 있다고 했을 때)
(a, b, A종류옷안입음) * (c, d, B종류옷안입음) = 9
마지막에 -1 을 해주면 답이 8이 됩니다. (뭐라도 하나 걸쳐야 하니까)

모든 경우의 수는
[ [“a”], [“b”], [“c”], [“d”], [“a”, “c”], [“a”, “d”], [“b”, “c”], [“b”, “d”]] => 8이죠.

len(d[key]) + 1 해주면 (~~~입는경우, 안입는경우) 가 되고,
최종적으로 -1 을 해주면 모든 의상을 안입는경우가 제외됩니다.
'''