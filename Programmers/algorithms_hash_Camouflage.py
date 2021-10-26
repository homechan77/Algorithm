# 위장

def solution(clothes):
    answer = {}
    # key(의상 종류)별 value(의상)의 개수 계산한다.
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    # 앞서 계산한 의상 개수에 아무것도 안입는 경우까지 1을 더하여 경우의 수를 계산한다.
    # headgear_(2+1) * eyewear_(1+1) = 6
    # 적어도 옷 하나는 걸치고 있어야 하므로 아무것도 안입는 경우 1을 빼준다. 
    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))