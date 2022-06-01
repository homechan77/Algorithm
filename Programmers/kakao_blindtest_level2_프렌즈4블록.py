# 테스트 케이스 5,8,10,11번 통과하지 못하는 코드
def solution(m, n, board):
    answerlist = []
    for i in range(len(board)-1):
        for j in range(len(board[i])-1):
            for l in range(i, len(board)):
                if board[i][j] == board[l][j+1]:
                    for k in range(l+1, len(board)):
                        if board[k][j:j+2] == (board[i][j])*2:
                            answerlist.extend([(i,j),(l,j+1),(k,j),(k,j+1)])
                            break
   
    answerset = set(answerlist)
    answer = len(answerset)
    return answer


##--------------------------------------------------------------------------##


# 정답 코드
from collections import deque

def solution2(m, n, board):
    answer = 0
    # board 내 각 요소들을 split하여 리스트로 재구성
    board = [list(w) for w in board]
    # 2x2의 창이 board를 스캔하며 4개의 원소 값이 모두 같은 경우, 해당 원소들의 좌표을 blocklist에 저장
    while True:
        blocklist = []
        for i in range(n-1):
            for j in range(m-1):
                tmp = [board[j][i], board[j][i+1], board[j+1][i], board[j+1][i+1]]
                block = [(j,i), (j,i+1), (j+1,i), (j+1, i+1)]
                if len(set(tmp)) == 1 and tmp[0] != 0:
                    blocklist.extend(block)
        # blocklist에 아무것도 없는 경우 정답을 return
        if len(blocklist) == 0:
            return answer
        
        # 중복 좌표 제거
        blocklist = list(set(blocklist))
        
        answer += len(blocklist)
        
        # blocklist 좌표들의 값을 0으로 치환
        for b in blocklist:
            board[b[0]][b[1]] = 0
            
        # 칼럼을 기준으로 모든 행 값을 tmp에 저장하고, tmp 값을 역순으로 빼내어 0이 아닌 것은 tmp2로, 0인 것은 count하여 그 count 수만큼 다시 tmp2에 삽입.
        # tmp2 값들을 기존 행 값에 넣어 재정립
        for c in range(n):
            tmp = []
            for r in range(m):
                tmp.append(board[r][c])
            queue = deque(tmp)
            tmp2 = []
            count = 0
            while queue:
                pop = queue.pop()
                if pop != 0:
                    tmp2.append(pop)
                else:
                    count += 1
            tmp2.extend([0]*count)
            for r in range(m):
                x = abs(r-m)-1
                board[r][c] = tmp2[x]                     

m = 8
n = 2
board = ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]
print(solution2(m, n, board))