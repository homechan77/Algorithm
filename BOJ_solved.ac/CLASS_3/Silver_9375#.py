# 패션왕 신해빈

'''
# 시도1. 메모리 초과
import sys; input = sys.stdin.readline
from collections import defaultdict
from itertools import combinations

tn = int(input())

for _ in range(tn):
    n = int(input())
    dic = defaultdict(list)
    for _ in range(n):
        a, b = input().rstrip().split()
        dic[b].append(a)
    keyn = len(dic.keys())
    result = n
    if keyn == 1:
        print(result)
        continue
    for i in range(2, keyn+1):
        combi = list(combinations(dic.keys(), i))
        for j in combi:
            tmp = 1
            for k in j:
                tmp *= len(dic[k])
            result += tmp
    print(result)
'''

##--------------------------------------------------------------------------##
# hat headgear
# sunglasses eyewear
# turban headgear
# 이렇게 있을 때 처음에는 headgear가 2개 eyewear가 1개라고 생각을 했는데, 안 입는 경우도 각각 포함시키도록 하면 된다. 그러니까 headgear에 대해서는 3가지 방법이 있는 것이다. 1. hat을 착용하는 방법 2. turban을 착용하는 방법 3. 착용하지 않는 방법. 마찬가지로 eyewear도 적용을 한다. 1. sungalsses를 착용하는 방법, 2. 착용하지 않는 방법.
# 이렇게 하면 headgear와 eyewear를 착용하거나 착용하지 않는 경우의 수는 (3*2)가 된다.
# 하지만 여기서 headgear를 착용하지 않고, eyewear도 착용하지 않는 여기서 말하는 알몸인 경우가 1개 존재하기 때문에 그 경우를 빼준다면 (3*2-1)이 된다.

import sys; input = sys.stdin.readline
from collections import defaultdict

tn = int(input())

for _ in range(tn):
    dic = defaultdict(list)
    n = int(input())
    for _ in range(n):
        a, b = input().rstrip().split()
        dic[b].append(a)
    result = 1
    for i in list(dic.keys()):
        result *= len(dic[i])+1
    print(result-1)
