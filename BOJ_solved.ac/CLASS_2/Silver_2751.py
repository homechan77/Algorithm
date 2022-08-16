import sys

n = int(sys.stdin.readline())
nlist = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=False)
for i in nlist:
    print(i)