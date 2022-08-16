import sys

n = int(sys.stdin.readline())
nlist = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)],
               key=lambda x: (x[1], x[0]))
for i in nlist:
    print(" ".join(map(str, i)))