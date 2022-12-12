def solution(record):
    idname, actions = {}, {}
    cnt = 1
    for i in record:
        spliti = i.split(' ')
        if spliti[0] == "Leave":
            act, id = spliti
            actions[cnt] = (act, id)
            cnt += 1
        else:
            act, id, name = spliti
            idname[id] = name
            if act == "Enter":
                actions[cnt] = (act, id)
                cnt +=1

    result = []
    for j in range(1, cnt):
        act, id = actions[j]
        if act == "Enter":
            result.append(idname[id]+"님이 들어왔습니다.")
        else:
            result.append(idname[id]+"님이 나갔습니다.")

    return result 

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))