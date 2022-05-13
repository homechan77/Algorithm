from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
       
    diffn = len(begin) - 1

    def certification(a, b):
        a = list(a)
        b = list(b)
        diffcount = 0
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                if i==j and  x==y:
                    diffcount += 1
        if diffcount == diffn:
            return True
        else:
            return False

    queue = deque()
    
    for j in words:
        if certification(begin, j):
            queue.append([j, 1])
            words.remove(j)    

    while queue:
        x = queue.popleft()
        if x[0] == target:
            break
        if len(words) == 0:
            continue
        for k in words:
            if certification(x[0], k):
                queue.append([k,(x[1]+1)])
                words.remove(k)


    return x[1]

"""
def solution(begin, target, words):
    if target not in words:
        return 0
    
    begin = set(begin)
    target = set(target)    
    new_words = []
    for i in words:
        new_words.append(set(i))
    
    diffn = len(begin) - 1
    
    count = 0
    
    queue = deque()
    
    for j in new_words:
        if len(begin.intersection(j)) == diffn:
            queue.append([j, 1])
            new_words.remove(j)    

    while queue:
        x = queue.popleft()
        if x[0] == target:
            break
        if len(new_words) == 0:
            continue
        for k in new_words:
            if len(x[0].intersection(k)) == diffn:
                queue.append([k,(x[1]+1)])
                new_words.remove(k)

                
    return x[1]
"""

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))