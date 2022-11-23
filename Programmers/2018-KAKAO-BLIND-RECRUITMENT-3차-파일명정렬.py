# [3차] 파일명 정렬

from collections import defaultdict

def solution(files):
    dic = defaultdict(list)
    for i, x in enumerate(files):
        flag = False
        start, end = 0, 0
        for j in range(len(x)):
            try:
                n = int(x[j])
                if not flag:
                    start = j
                    flag = True
                    continue
                # NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자
                if flag:
                    if j-start+1 == 5:
                        end  = j
                        flag = False
                        break
            except ValueError:
                if flag:
                    end = j-1
                    flag = False
                    break
                continue
        if flag: # 파일명이 숫자로 끝나는 경우
            dic[x[:start].lower()].append((int(x[start:]), i))
        else:
            dic[x[:start].lower()].append((int(x[start:end+1]), i))

    result = []
    dickeyssort = sorted(list(dic.keys()))
    for i in dickeyssort:
        tmp = sorted(dic[i], key=lambda x: (x[0], x[1]))
        for j in tmp:
            result.append(files[j[1]])

    return result

files = ["O00321", "O49qcGPHuRLR5FEfoO00321"]
# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))
