# import copy

n = int(input())
inputlist = [int(input()) for _ in range(n)]

# def solution(n, inputlist):
#     inputlistcopy = copy.deepcopy(inputlist)
#     stackbox = []
#     labeling = []
#     answer = []
#     printanswer = []
#     for i in range(n):
#         a = i+1
#         if a == inputlist[-1]:
#             if len(labeling) > 0:
#                 while labeling:
#                     pop = labeling.pop()
#                     printanswer.append('-')
#                     answer.append(pop)
#                 inputlist.pop()
#                 stackbox.append(a)
#                 printanswer.append('+')
#             else:
#                 inputlist.pop()
#                 stackbox.append(a)
#                 printanswer.append('+')
#         else:
#             labeling.append(a)
#             printanswer.append('+')
#     while stackbox:
#         pop2 = stackbox.pop()
#         answer.append(pop2)
#         printanswer.append('-')
        
#     if answer == inputlistcopy:
#         for i in printanswer:
#             print(i)
#     else:
#         print('NO')


     
def solution2(n, inputlist):
    cnt = 0
    stack = []
    result = []
    for i in inputlist:
        while cnt < i:
            cnt += 1
            stack.append(cnt)
            result.append('+')
        if stack[-1] == i:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            return
    
    for j in result:
        print(j)

solution2(n, inputlist)