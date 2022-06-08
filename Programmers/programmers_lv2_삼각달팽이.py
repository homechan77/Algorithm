def down(pyramid, n, x, y, a):
    for i in range(n):
        if y == 0:
            pyramid[x][y] = (a+1)
            a = pyramid[x][y]
            if i == n-1:
                break
            x += 1
        else:
            pyramid[x+1][y] = (a+1)
            a = pyramid[x+1][y]
            x += 1
    n -= 1
    return n,x,y,a

def right(pyramid, n, x, y, a):
    for _ in range(n):
        pyramid[x][y+1] += (a+1)
        a = pyramid[x][y+1]
        y += 1
    
    n -= 1
    return n,x,y,a

def up(pyramid, n,x,y,a):
    for _ in range(n):
        pyramid[x-1][y-1] = (a+1)
        a = pyramid[x-1][y-1]
        x -= 1
        y -= 1
        
    n -= 1
    return n,x,y,a


def solution(n):
    pyramid = [[0]*n for _ in range(n)]
    ncopy = n
    x = 0
    y = 0
    a = 0
    pyramid[x][y] = a
    
    while True:
        n, x, y, a = down(pyramid, n, x, y, a)
        if n<1:
            break
        
        n, x, y, a = right(pyramid, n, x, y, a)
        if n<1:
            break
        
        n, x, y, a = up(pyramid, n, x, y, a)
        if n<1:
            break
    
    answer = []
    for k in range(ncopy):
        answer.extend(pyramid[k][:k+1])
    
        
    return answer


n = 6
print(solution(n))