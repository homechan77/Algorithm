# 시간초과

def solution(n,a,b):
    nhol = list(filter(lambda x: x%2==1, range(n+1)))
    roundlist = [(i,i+1) for i in nhol]
    
    cnt = 1
    
    while True:
        tmp = []
        for j in roundlist:
            if len(tmp)==0 or len(tmp[-1]) >= 2:
                if j[0] == a or j[1] == a:
                    tmp.append([a])
                elif j[0] == b or j[1] == b:
                    tmp.append([b])
                else:
                    tmp.append([max(j)])
            else:
                if j[0] == a or j[1] == a:
                    tmp[-1].append(a)
                elif j[0] == b or j[1] == b:
                    tmp[-1].append(b)
                else:
                    tmp[-1].append(max(j))
        
            if tmp[-1] == [a, b]:
                cnt += 1
                return cnt
        
        cnt += 1
        roundlist = tmp

##--------------------------------------------------------------------------##
# 다른 사람들 문제 해결법 참고

def solution2(n, a, b):
    nlist = [i+1 for i in range(n)]
    cnt = 0
    nlistcopy = nlist
    while True:
        tmp = [(i//2)+(i%2) for i in nlistcopy]
        cnt += 1
        if tmp[a-1] == tmp[b-1]:
            return cnt
        nlistcopy = tmp

def solution3(n, a, b):
    cnt = 0
    while a != b:
        a, b = (a//2)+(a%2), (b//2)+(b%2)
        cnt += 1
    return cnt


n = 8
a = 4
b = 7
print(solution3(n, a, b))
