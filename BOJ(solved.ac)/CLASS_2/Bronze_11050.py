import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().split())
nlist = [str(i) for i in range(n)]
answer = len(list(combinations(nlist, k)))
print(answer)