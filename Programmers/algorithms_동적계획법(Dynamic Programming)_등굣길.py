def solution(m, n, puddles):
    list2d = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        list2d.append(temp)

    for a in puddles:
        list2d[a[1]-1][a[0]-1] = 999
    
    for x in range(len(list2d)):
        for y in range(len(list2d[x])):
            list2d[0][0] = 1
            
            if list2d[x][y] == 999:
                continue
            # if x == n-1 and y == m-1:
            #     return (list2d[x-1][y] + list2d[x][y-1]) % 1000000007
            
            try:
                if list2d[x+1][y] != 999:
                    list2d[x+1][y]+=list2d[x][y]
            except IndexError:
                pass
                # if list2d[x][y+1] != 999:
                #     list2d[x][y+1]+=1
                    
            try:
                if list2d[x][y+1] != 999:
                    list2d[x][y+1]+=list2d[x][y]
            except IndexError:
                pass
                # if list2d[x+1][y] != 999:
                #     list2d[x+1][y]+=1
                
    return list2d[n-1][m-1] % 1000000007

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))

# return = 4