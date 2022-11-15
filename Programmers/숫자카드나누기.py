# def divisor(x):
#     arr = []
#     for i in range(1, x+1):
#         if x % i == 0:
#             arr.append(i)
#     return arr

# def makeintersec(array):
#     intersec = set([])
#     for i, x in enumerate(array):
#         if i == 0:
#             intersec = set(divisor(x))
#             continue
#         intersec = intersec.intersection(set(divisor(x)))
#     return intersec

# def check(divi, array):
#     for i in divi:
#         if i == 1:
#             return 0
#         flag = False
#         for j in array:
#             if j%i == 0:
#                 flag = True
#                 break
#         if not flag:
#             return i

import math

def gcd(array):
    g = array[0]
    for i in range(2, len(array)):
        g = math.gcd(g, array[i])
    return g


def solution(arrayA, arrayB):
    Aintersec = gcd(arrayA)
    Bintersec = gcd(arrayB)
    # Aintersec = sorted(list(makeintersec(arrayA)))[-1]
    # Bintersec = sorted(list(makeintersec(arrayB)))[-1]
    
    maxn = 0
    flag = False
    for i in arrayB:
        if i%Aintersec == 0:
            flag = True
            break
    if not flag:
        maxn = max(maxn, Aintersec)
    flag = False
    for i in arrayA:
        if i%Bintersec == 0:
            flag = True
            break
    if not flag:
        maxn = max(maxn, Bintersec)

    return maxn

arrayA = [10, 20]
arrayB = [5, 17]
print(solution(arrayA, arrayB))