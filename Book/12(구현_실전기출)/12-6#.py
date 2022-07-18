# 기둥과 보 설치

# 기둥 = {1. 바닥 위}, {2. 보의 한쪽 끝 부분 위}, {3. 다른 기둥 위}
# 보 = {1. 한쪽 끝 부분이 기둥 위}, {2. 양쪽 끝 부분이 다른 보와 동시에 연결}
# 위 조건이 지켜지지 않는 작업 결과는 무시된다.
##--------------------------------------------------------------------------##
# 시도1. 실패
# def check(n, wall, x, y, a):
#     # 기둥
#     if a == 0:
#         # 바닥 위
#         if y == n:
#             return True
#         # 보의 한쪽 위
#         elif wall[y][x-1]==1 or wall[y][x]==1:
#             return True
#         # 다른 기둥 위
#         elif wall[y+1][x] == 0:
#             return True
#         else:
#             return False
#     # 보
#     else:
#         # 한쪽 끝 부분이 기둥 위
#         if wall[y+1][x]==0 or wall[y+1][x+1]==0:
#             return True
#         # 양쪽 끝 부분이 다른 보와 동시에 연결
#         elif wall[y][x-1]==1 and wall[y][x+1]==1:
#             return True
#         else:
#             return False

# def solution(n, build_frame):
#     wall = [[999]*(n+3) for _ in range(n+3)]
#     structure = []
#     for i in build_frame:
#         x = i[0]
#         y = abs(i[1]-n)
#         # 설치 시에는 주어진 좌표에서 기둥이나 보가 들어갈 수 있는지만 확인
#         if i[3] == 1:
#             answer = check(n, wall, x, y, i[2])
#             if answer is True:
#                 wall[y][x] = i[2]
#                 structure.append([x,i[1],i[2]])
#         # 삭제 시에는 주어진 좌표에서 해당 기둥이나 보를 삭제할 경우 나머지 모든 기둥이나 보가 조건을 만족하는지 확인
#         else:
#             wall[y][x] = 999
#             structure.remove([x,i[1],i[2]])
#             for j in structure:
#                 x2 = j[0]
#                 y2 = abs(j[1]-n)
#                 answer = check(n, wall, x2, y2, j[2])
#                 if answer is False:
#                     wall[y][x] = i[2]
#                     structure.append([x,i[1],i[2]])
#                     break

#     result = sorted(structure, key=lambda x: ([x[0],x[1],x[2]]))
#     return result

##--------------------------------------------------------------------------##
# 시도2. 책 참고_(설치시 왜 다른 구조물들에 대해서도 조건 만족을 체크해야 하는지 의문이다.)
def check(answer):
    for x, y, what in answer:
        # 기둥
        if what == 0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        # 보
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, what, how = i
        # 설치
        if how == 1:
            answer.append([x,y,what])
            if not check(answer):
                answer.remove([x,y,what])
        # 삭제
        else:
            answer.remove([x,y,what])
            if not check(answer):
                answer.append([x,y,what])
    result = sorted(answer, key=lambda x: ([x[0],x[1],x[2]]))
    return result
            
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))
