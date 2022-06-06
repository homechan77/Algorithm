from itertools import combinations
from collections import deque, defaultdict, Counter

# 내가 짠 코드
def solution(orders, course):
    list1 = []
    for i in course:
        list2 = []
        # "i" 조합의 경우를 list2에 모두 저장한다. 
        # orders의 원소를 정렬한 후 조합할 경우 ('x', 'w') ('w', 'x')와 같은 경우를 비교하지 않아도 된다.
        for j in orders:
            list2.extend(list(combinations(sorted(j), i)))

        # list2를 하나씩 빼가면서 갯수를 딕셔너리의 value로 구해본다. 
        queue = deque(list2)
        dict1 = defaultdict(int)
    
        while queue:
            pop = queue.popleft()
            if len(dict1)==0:
                dict1[pop]=1
                continue
            if pop in dict1.keys():
                dict1[pop] += 1
            else:
                dict1[pop] = 1
        
        # 딕셔너리의 value를 기준으로 내림차순으로 정렬한 리스트를 생성하고 value가 2이상이면서 최대값이 중복될 경우 해당 경우의 key를 모두 list1에 저장한다. 
        # 내림차순 정렬한 상태이기 때문에 최대값과 같지 않다면 반복문 종료
        if len(dict1) == 0:
            continue
        sort_dict1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        maxkey = sort_dict1[0]
        if maxkey[1] >= 2:
            for x, y in sort_dict1[1:]:
                if y == maxkey[1]:
                    list1.append(x)
                else:
                    break
            list1.append(maxkey[0])
        
        
    list1 = sorted(list(map(lambda x: ''.join(x), list1)))
    return list1

##--------------------------------------------------------------------------##
# 다른 정답자가 짠 코드
def solution2(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
