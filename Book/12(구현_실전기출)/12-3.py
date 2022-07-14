from collections import deque

def solution(s):
    slist = list(s)
    answerlist = []
    for i in range(1, len(slist)+1):
        tmp = []
        start = 0
        icopy = i
        while start <= len(slist):
            tmp.append(''.join(slist[start:i]))
            start = i
            i += icopy
        tmp2 = []
        queue = deque(tmp)
        while queue:
            pop = queue.popleft()
            if len(tmp2)==0 or tmp2[-1][1]!=pop:
                tmp2.append([1, pop])
            else:
                tmp2[-1][0] += 1
        tmp3 = []
        for j in tmp2:
            if j[0] > 1:
                tmp3.append(str(j[0])+j[1])
            else:
                tmp3.append(j[1])
        answerlist.append(''.join(tmp3))
    
    answer = min(list(map(lambda x: len(x), answerlist)))
    return answer

s = "xababcdcdababcdcd"
print(solution(s))