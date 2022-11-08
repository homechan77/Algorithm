# 비밀번호 찾기

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
infodict = {}
for _ in range(n):
    site, password = input().rstrip().split()
    infodict[site] = password
for _ in range(m):
    question = input().rstrip()
    print(infodict[question])