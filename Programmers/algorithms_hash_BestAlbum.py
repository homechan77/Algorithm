# 나의 코드 - 실패


def solution(genres, plays):
    list1 = []
    for i, j in zip(genres, plays):
        list1.append((i, j))

    dict1 = {}

    for g, p in list1:
        if g in dict1:
            dict1[g] += p
        else:
            dict1[g] = p

    sort_dict1 = sorted(dict1.items(), reverse=True)

    list2 = []

    for k in range(len(sort_dict1)):
        list2.append([])
        for l in range(len(list1)):
            if list1[l][0] == sort_dict1[k][0]:
                list2[k].append((list1[l][1], l))
    
    for s in range(len(list2)):
        list2[s] = sorted(list2[s], key=lambda x: (-x[0], x[1]))

    answer = []
    for a in range(len(list2)):
        count = 0
        for b in list2[a]:
            if count < 2:
                answer.append(b[1])
                count += 1
            else:
                break
    
    return answer


##--------------------------------------------------------------------------##
# 정답자 코드

def solution(genres, plays):
    answer = []

    genre_total_play = {}
    genre_dic = {}

    # 
    for i in range(len(genres)):
        if genres[i] not in genre_dic.keys():
            genre_dic[genres[i]] = [(plays[i], i)]
            genre_total_play[genres[i]] = plays[i]

        else:
            genre_dic[genres[i]].append((plays[i], i))
            genre_total_play[genres[i]] += plays[i]
    
    sorted_total_play = sorted(genre_total_play.items(), key=lambda x:x[1], reverse=True)

    for key in sorted_total_play:
        play_list = genre_dic[key[0]]
        play_list = sorted(play_list, key=lambda x: (-x[0], x[1]))

        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])


    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

