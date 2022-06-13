testcase = []
while True:
    inputn = input()
    testcase.append(inputn)
    if inputn == '0':
        break

def solution(testcase):
    testcase.pop()
    for i in testcase:
        if i == i[::-1]:
            print('yes')
        else:
            print('no')
    return

solution(testcase)
