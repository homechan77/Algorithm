# 입력
# N:행(세로), M:열(가로)
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 주어진 board를 8x8로 쪼갤 수 있는 모든 경우의 수 
def makeeightboard(board):
    eightboard = []
    for i in range((N-8)+1):
        tmp = board[i:i+8]
        for j in range((M-8)+1):
            eightboard.append(list(map(lambda x:x[j:j+8], tmp)))
    return eightboard


def solution(N, M , board):
    eightboard = makeeightboard(board)    
    color = ['W', 'B']
    
    answer = []
    # 8x8 사이즈로 자른 체스판을 하나씩 호출
    for i, m in enumerate(eightboard):
        cnt = 0
        cnt2 = 0
        setcolor = m[0][0]
        notsetcolor = color[1-color.index(setcolor)]
        
        # 체스판의 [0][0]의 색을 'B', 'W' 두가지 경우로 나누어 색을 칠해야 하는 수를 카운트
        # 짝수 행
        for j, n in enumerate(m[0::2]):
            # 경우 1
            if n[0] != setcolor:
                cnt += 1
                
            # 짝수 열(첫번째 열은 제외_이미 위에서 카운트) 
            cnt += len(list(filter(lambda x: x!=setcolor, n[2::2])))
            # 홀수 열
            cnt += len(list(filter(lambda x: x==setcolor, n[1::2])))
            
            # 경우 2
            if n[0] != notsetcolor:
                cnt2 += 1
            cnt2 += len(list(filter(lambda x: x!=notsetcolor, n[2::2])))
            cnt2 += len(list(filter(lambda x: x==notsetcolor, n[1::2])))
            
            
        # 홀수 행
        for j, n in enumerate(m[1::2]):
            # 경우 1
            if n[0] == setcolor:
                cnt += 1
            
            # 짝수 열(첫번째 열은 제외_이미 위에서 카운트) 
            cnt += len(list(filter(lambda x: x!=notsetcolor, n[2::2])))
            # 홀수 열
            cnt += len(list(filter(lambda x: x==notsetcolor, n[1::2])))
            
            # 경우 2
            if n[0] == notsetcolor:
                cnt2 += 1
            cnt2 += len(list(filter(lambda x: x!=setcolor, n[2::2])))
            cnt2 += len(list(filter(lambda x: x==setcolor, n[1::2]))) 
                
        mincnt = min(cnt, cnt2)
        answer.append(mincnt)
        
    return min(answer)
                
print(solution(N, M, board))