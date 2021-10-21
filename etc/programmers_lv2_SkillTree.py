~~~
# 내가 생각한 구현 방법 _ 실패!!!
def solution(skill, skill_trees):
    skill = list(skill)

    count = 0

    while skill_trees:
        for i in skill_trees:
            for j in skill[:-1]:


                if j in i:
                    indexing = i.index(j)
                    if indexing == 0:
                        continue

                    listx = i[:indexing]
                    if len([[s] for s in skill[skill.index(j)+1:] if s in listx]) > 0:
                        #1. del skill_trees[0]
                        break

            else:
                count += 1
                #2. del skill_trees[0]
        del skill_trees[0]
    
    return count

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
~~~

##--------------------------------------------------------------------------##
# 구현 참조 1 (이해가 안된다...)
def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        idx = 0
        ispossible = True
        for stt in st:
            # stt가 skill 내의 요소에 해당하지 않은면 continue
            if stt not in skill:
                continue
            # stt가 skill 내의 요소에 해당할 때, idx와 stt 요소의 skill 내의 인덱싱 번호를 비교하여 두개가 같거나 idx가 클 경우 idx를 1씩 증가시키고 반대의 경우 ispossible을 False로 변환 반복문을 빠져 나간다.
            if idx < skill.index(stt):
                ispossible = False
                break
            else:
                idx += 1
        
        if ispossible:
            answer += 1

    return answer

    
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))

##--------------------------------------------------------------------------##
# 구현 참조 2
def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        list = []
        fin = True

        # skill_tree 요소들의 스킬들 중 skill에 해당하는 것들을 list 객체에 추가 
        for j in range(len(i)):
            if i[j] in skill:
                list.append(i[j])
        
        # list와 skill의 요소들을 하나하나 비교
        for k in range(len(list)):
            if list[k] != skill[k]:
                fin = False
                break

        if fin = True:
            answer += 1
    
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))



