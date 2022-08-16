import sys

n = int(sys.stdin.readline())
nlist = sorted([list(map(int, sys.stdin.readline().split())) for i in range(n)], 
               key=lambda x: (x[0], x[1]),
               reverse=True)

def solution(nlist):
        for i in nlist[-1::-1]:
                print(i[0], i[1])
                
solution(nlist)