def solution(triangle):
    for i in range(len(triangle)):
        if i == (len(triangle) - 1):
            break
        
        ipluslist = []
        for x in triangle[i+1]:
            ipluslist.append(x)
        # ipluslist = triangle[i+1]
        
        for j in range(len(triangle[i])):
            i_a = ipluslist[j]
            i_b = ipluslist[j+1]
            if triangle[i][j] + i_a > triangle[i+1][j]:
                triangle[i+1][j] = triangle[i][j] + i_a
            if triangle[i][j]+i_b > triangle[i+1][j+1]:
                triangle[i+1][j+1] = triangle[i][j] + i_b
            
    # return triangle
    return max(triangle[len(triangle)-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	
print(solution(triangle))

#result = 30