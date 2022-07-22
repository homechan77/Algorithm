import sys

s = list(sys.stdin.readline().strip())
def solution(s):
    alphabet = []
    numsum = 0
    for i in s:
        try:
            numsum += int(i)
        except ValueError:
            alphabet.append(i)
    alphabet.sort()
    answer = ''.join(alphabet)+str(numsum)
    return answer

print(solution(s))

# K1KA5CB7
# AJKDLSI412K4JSJ9D