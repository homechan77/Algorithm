a,b = map(int, input().split())

dimension = [[0]*b for _ in range(a)]

x,y,direction = map(int, input().split())
dimension[x][y] = 1

list_m = []
for _ in range(b):
    list_m.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
#move = [0,1,2,3]

count = 1
turn_time = 0

def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

while True:
    turn_left()
    list_m[x][y] = 4
    nx,ny = x+dx[direction], y+dy[direction]
    if dimension[nx][ny] == 0 and list_m[nx][ny] == 0:
        x,y = nx, ny
        count += 1
        turn_time  = 0
        continue
    else: 
        turn_time += 1
    if turn_time == 4:
        nx, ny = x-dx[direction], y-dy[direction]
        if list_m[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)
