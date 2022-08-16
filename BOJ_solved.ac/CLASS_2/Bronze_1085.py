x,y,w,h = map(int, input().split(' '))
def solution(x,y,w,h):
    up = y-0
    down = h-y
    right = x-0
    left = w-x
    slist = [up, down, right, left]
    return min(slist)

print(solution(x,y,w,h))