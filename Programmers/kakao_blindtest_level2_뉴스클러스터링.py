from collections import Counter

def solution(str1, str2):
    alpha = [k for k in range(65, 91)]

    strlist = [str1, str2]
    strcombi = [[] for _ in range(2)]
    for i in range(len(strlist)):
        strlist[i] = strlist[i].upper()
        for j in range(len(strlist[i])-1):
            if ord(strlist[i][j]) in alpha and ord(strlist[i][j+1]) in alpha:
                strcombi[i].append((strlist[i][j], strlist[i][j+1]))

    str1info = Counter(strcombi[0])
    str2info = Counter(strcombi[1])

    str1key = list(Counter(strcombi[0]).keys())
    str2key = list(Counter(strcombi[1]).keys())

    gyolist = list(set(str1key).intersection(set(str2key)))
    haplist = list(set(str1key).union(set(str2key)))

    if len(str1info)==0 and len(str2info)==0:
        return 65536
    gyo = 0
    for x in gyolist:
        gyo += min(str1info[x], str2info[x])
    hap = 0
    for y in haplist:
        if y in str1key and y in str2key:
            hap += max(str1info[y], str2info[y])
        elif y in str1key:
            hap += str1info[y]
        else:
            hap += str2info[y]


    answer = int((gyo / hap) * 65536)

    return answer

str1 = 'A+C'
str2 = 'DEF'
print(solution(str1, str2))