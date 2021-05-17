a,b = map(int, input().split())

lista = []
for _ in range(a):
    lista.append(list(map(int, input())))
#lista = [list(map(int,input())) for _ in range(N)]

def dfs(x, y):
    if x <= -1 or x >= a or y <= -1 or y >= b:
        return False
    if lista[x][y] == 0:
        lista[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0

for i in range(a):
    for j in range(b):
        if dfs(i, j) == True:
            result += 1

print(result)