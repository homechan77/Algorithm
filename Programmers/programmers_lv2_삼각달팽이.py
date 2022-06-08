# def down(pyramid, n, x, y, a):
#     for i in range(n):
#         if y == 0:
#             pyramid[x][y] = (a+1)
#             a = pyramid[x][y]
#             if i == n-1:
#                 break
#             x += 1
#         else:
#             pyramid[x+1][y] = (a+1)
#             a = pyramid[x+1][y]
#             x += 1
#     n -= 1
#     return n,x,y,a

# def right(pyramid, n, x, y, a):
#     for _ in range(n):
#         pyramid[x][y+1] += (a+1)
#         a = pyramid[x][y+1]
#         y += 1
    
#     n -= 1
#     return n,x,y,a

# def up(pyramid, n,x,y,a):
#     for _ in range(n):
#         pyramid[x-1][y-1] = (a+1)
#         a = pyramid[x-1][y-1]
#         x -= 1
#         y -= 1
        
#     n -= 1
#     return n,x,y,a


# def solution(n):
#     pyramid = [[0]*n for _ in range(n)]
#     ncopy = n
#     x = 0
#     y = 0
#     a = 0
#     pyramid[x][y] = a
    
#     while True:
#         n, x, y, a = down(pyramid, n, x, y, a)
#         if n<1:
#             break
        
#         n, x, y, a = right(pyramid, n, x, y, a)
#         if n<1:
#             break
        
#         n, x, y, a = up(pyramid, n, x, y, a)
#         if n<1:
#             break
    
#     answer = []
#     for k in range(ncopy):
#         answer.extend(pyramid[k][:k+1])
    
        
#     return answer


# n = 6
# print(solution(n))

##--------------------------------------------------------------------------##
# 클래스를 활용하여 코드 정리

class Triangle():
    def __init__(self, n):
        self.ncopy = n
        self.pyramid = [[0]*n for _ in range(n)]
        self.x = 0
        self.y = 0
        self.cnt = 0
    
    def down(self):
        for i in range(self.ncopy):
            if self.y == 0:
                self.pyramid[self.x][self.y] = (self.cnt+1)
                self.cnt = self.pyramid[self.x][self.y]
                if i == self.ncopy-1:
                    break
                self.x += 1
            else:
                self.pyramid[self.x+1][self.y] = (self.cnt+1)
                self.cnt = self.pyramid[self.x+1][self.y]
                self.x += 1
        
        self.ncopy -= 1
        return self.ncopy

    def right(self):
        for _ in range(self.ncopy):
            self.pyramid[self.x][self.y+1] += (self.cnt+1)
            self.cnt = self.pyramid[self.x][self.y+1]
            self.y += 1
    
        self.ncopy -= 1
        return self.ncopy
    
    def up(self):
        for _ in range(self.ncopy):
            self.pyramid[self.x-1][self.y-1] = (self.cnt+1)
            self.cnt = self.pyramid[self.x-1][self.y-1]
            self.x -= 1
            self.y -= 1
        
        self.ncopy -= 1
        return self.ncopy

def solution(n):
    triangle = Triangle(n)
    while True:
        a = triangle.down()
        if a < 1:
            break
        a = triangle.right()
        if a < 1:
            break
        a = triangle.up()
        if a < 1:
            break
    
    pyramid = triangle.pyramid
    
    answer = []
    for k in range(n):
        answer.extend(pyramid[k][:k+1])
    
    return answer

n = 5
print(solution(n))