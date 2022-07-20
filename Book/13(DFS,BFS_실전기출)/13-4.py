from collections import deque

def seperation(a):
    queue = deque(a)
    cnt1, cnt2 = 0, 0
    while queue:
        pop = queue.popleft()
        if pop == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            break
    result = cnt1 + cnt2
    return result
    
def check_right_string(b):
    queue = deque(b)
    tmp = []
    while queue:
        pop = queue.popleft()
        if pop == '(':
            tmp.append(pop)
        else:
            if len(tmp) == 0:
                return False
            tmp.pop()
    if len(tmp) > 0:
        return False
    else:
        return True

def make_right_string(c, d):
    tmp = ['(']
    tmp.extend(list(solution(d)))
    tmp.append(')')
    del c[0]
    del c[-1]
    for i in c:
        if i == '(':
            tmp.append(')')
        else:
            tmp.append('(')
    
    result = "".join(tmp)
    return result
    
def solution(p):
    listp = list(p)
    if len(listp) == 0:
        return ""
    un = seperation(listp)
    u, v = listp[:un], listp[un:]
    
    if check_right_string(u) is True:
        u = "".join(u)
        v = solution(v)
        return u+v
    else:
        v = solution(v)
        u = make_right_string(u, v)
        return u


p = "()))((()"
print(solution(p))