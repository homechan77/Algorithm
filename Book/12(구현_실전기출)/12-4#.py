# 자물쇠와 열쇠(2020 KAKAO BLIND RECRUITMENT)

def rotate_a_matrix_by_90_degree(a):
    n = len(a) # input된 기존 a의 '행' 길이
    m = len(a[0]) # input된 기존 a의 '열' 길이
    result = [[0]*n for _ in range(m)] # 90도 회전 후의 도형(n이 열의 길이, m이 행의 길이가 된다)
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j] # ex) [0,0] -> [0,2]
    return result
    
def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    # 자물쇠와 열쇠는 정사각형
    n = len(lock)
    m = len(key)
    
    # 자물쇠의 크기를 3배로 변환하고 기존의 자물쇠를 중앙에 삽입
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 열쇠를 회전시키면서 자물쇠에 끼워보기
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2): # "n*2" = 열쇠가 변환된 자물쇠를 스캔하는 데 정해진 한정 범위
                # 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 열쇠가 자물쇠에 정확히 맞는지 확인
                if check(new_lock) == True:
                    return True
                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]     
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
# result: true