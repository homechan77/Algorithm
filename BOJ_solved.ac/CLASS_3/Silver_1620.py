# 나는야 포켓몬 마스터 이다솜

import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

pbook = defaultdict(list)
cnt = 1
for _ in range(n):
    pbook[input().rstrip()] = cnt
    cnt += 1

key_pbook = list(pbook.keys())

question = [input().rstrip() for _ in range(m)]

for i in question:
    if 65 <= ord(i[0]) <= 90:
        print(pbook[i])
    else:
        print(key_pbook[int(i)-1])