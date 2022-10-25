# IOIOI

'''
# 시도 1. 50점(시간 초과_O(n*m))
import sys; input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

plength = n+(n+1)
p = 'IO'*n+'I'
# pnlist = []
# for i in range(1, plength+1):
#     if i % 2 != 0:
#         pnlist.append('I')
#     else:
#         pnlist.append('O')
# p = ''.join(pnlist)

cnt = 0
for j in range(m-(plength-1)):
    if s[j:j+plength] == p:
        cnt += 1

print(cnt)
'''
##--------------------------------------------------------------------------##
# 시도 2. 정답자 풀이 참조
# https://resilient-923.tistory.com/231

import sys; input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

i = 0
cnt = 0
answer = 0
flag = 0

while i < m-2:
    if s[i] == 'I':
        flag = 1
    else:
        i += 1
    if flag == 1:
        if s[i+1] == 'O' and s[i+2] == 'I':
            cnt += 1
            if cnt == n:
                answer += 1
                cnt -= 1
            i += 2
        else:
            cnt = 0
            flag = 0
            i += 1

print(answer)
