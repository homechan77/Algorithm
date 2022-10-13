# 색종이 만들기

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

white, black = 0, 0

def dfs(n, start):
    global white, black

    row, col = start
    check = arr[row][col]
    # alarm = False

    for r in range(row, row+n):
        for c in range(col, col+n):
            if arr[r][c] != check:
                # alarm = True
                splitn = n // 2
                for i in [(row, col), (row, col+splitn), (row+splitn, col), (row+splitn, col+splitn)]:
                    dfs(splitn, i)
                return
                # break
        # if alarm:
        #     break

    # if not alarm:
    #     if check == 0:
    #         white += 1
    #     else:
    #         black += 1  
    if check == 0:
        white += 1
    else:
        black += 1

dfs(n, (0, 0))

print(white)
print(black)