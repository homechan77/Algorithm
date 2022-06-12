# skt 인턴십 코딩테스트(2022.6.12)
# ------------------------------------------------------ #

# 문제 1번

# def solution(p):
#     n = len(p)
#     answer = [0]*n

#     for i in range(n):
#         x = p[i]
#         if x == i+1:
#             continue
        
#         for j, y in enumerate(p[i+1:]):
#             if y == i+1:
#                 p[i] = y
#                 answer[i] += 1
#                 p[j+i+1] = x
#                 answer[j+i+1] += 1
#                 break

#     return answer

# p = [2,5,3,1,4]
# print(solution(p))

# ------------------------------------------------------ #
# 문제 2번

# def solution(periods, payments, estimates):
#     n = len(periods)
#     tmp = [[] for _ in range(n)]
#     answer = [0]*2

#     for i in range(n):
#         # 이번 달
#         nowmonth = periods[i]
#         nowpay = sum(payments[i])
#         if nowmonth >= 60:
#             if nowpay >= 900000:
#                 tmp[i].append('O')
#             elif 600000 <= nowpay < 900000:
#                 tmp[i].append('O')
#             else:
#                 tmp[i].append('X')

#         elif 24 <= nowmonth < 60:
#             if nowpay >= 900000:
#                 tmp[i].append('O')
#             else:
#                 tmp[i].append('X')

#         else:
#             tmp[i].append('X')

#         # 다음 달
#         nextmonth = nowmonth + 1
#         nextpay = sum(payments[i][1:])+estimates[i]
#         if nextmonth >= 60:
#             if nextpay >= 900000:
#                 tmp[i].append('O')
#             elif 600000 <= nextpay < 900000:
#                 tmp[i].append('O')
#             else:
#                 tmp[i].append('X')

#         elif 24 <= nextmonth < 60:
#             if nextpay >= 900000:
#                 tmp[i].append('O')
#             else:
#                 tmp[i].append('X')

#         else:
#             tmp[i].append('X')
    
#     for x in range(len(tmp)):
#         if tmp[x] == ['X', 'O']:
#             answer[0] += 1 
#         if tmp[x] == ['O', 'X']:
#             answer[1] += 1

#     return answer

# periods = [24, 59, 59, 60]
# payments = [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]
# estimates = [350000, 50000, 40000, 50000]
# print(solution(periods, payments, estimates))

# ------------------------------------------------------ #
# 문제 3번

# def solution(n, plans, clients):
    
#     plann = len(plans)
#     planlist = [[] for _ in range(plann)]
    
#     for i in range(plann):
#         if i == 0:
#             tmp = plans[i].split(' ')
#             planlist[i].append(int(tmp[0]))
#             planlist[i].append(tmp[1:])
#             continue
#         tmp = plans[i].split(' ')
#         planlist[i].append(int(tmp[0]))
#         planlist[i].append(tmp[1:])
#         planlist[i][1].extend(planlist[i-1][1])
    
#     answer = [0] * len(clients)

#     for i, x in enumerate(clients):
#         ix = x.split(' ')
#         data = int(ix[0])
#         service = ix[1:]
#         servicen = len(service)
#         for j, y in enumerate(planlist):
#             if data <= y[0]:
#                 cnt=0
#                 for k in service:
#                     if k in y[1]:
#                         cnt += 1
#                 if cnt == servicen:
#                     answer[i] = j+1
#                     break

#     return answer

# n=4
# plans = ["38 2 3", "394 1 4"]
# clients = ["10 2 3", "300 1 2 3 4", "500 1"]
# print(solution(n, plans, clients))


# ------------------------------------------------------ #
# 문제 4번(작성 실패)

route = []

def route(grid, start, tmp):
    global route
    if start == [0, 0]:
        tmp.append(start)
        def route(grid, start+1, tmp+1)
    
    route.pop()
    route(grid, start, tmp+1)
    
    return tmp
    
        
def solution(grid, k):
    route = route(grid, [0, 0], [])
    answer = -1
    return answer
    
grid = [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"]
k = 6
# result: 3