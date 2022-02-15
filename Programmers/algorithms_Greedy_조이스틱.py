#문제 자체가 이해가 안됨;;
"""
import string

def solution(name):
    listalphabet = list(string.ascii_uppercase)
    
    namelist = list(name)
    controlnamelist = ['A'] * len(name)    

    count = 0

    while controlnamelist != namelist:
        
        right = 0
        left = right + ((i - len(namelist)) * -1)
        
        for i in range(len(namelist)):
            if namelist[i] != 'A':
                up = listalphabet.index(namelist[i])
                down = (up - len(listalphabet)) * -1
                if up > down:
                    count += down
                else:
                    count += up
        
                controlnamelist[i] = namelist[i]

                right += 1
            else:
                right += 1
                    
        if indexnum != 0:
"""

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
    
    if (min_move < 0):
        return answer
        
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + (i + len(name)) - next)
    answer += min_move
    return answer


name = "JEROEN"
print(solution(name))