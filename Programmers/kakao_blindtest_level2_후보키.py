from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    # 1. issubset() 함수를 사용한 유일성과 최소성 확인
    # 가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
    
    # 유일성, 최소성 확인
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put: unique.append(i)
   
    return len(unique)

    # # 2. issubset() 함수를 사용하지 않고 유일성과 최소성 확인
    # # 유일성
    # final=[]
    # for keys in candidates:
    #     tmp=[tuple([item[key] for key in keys]) for item in relation]
    #     if len(set(tmp))==n_row:
    #         final.append(keys)

    # # 최소성
    # answer=set(final)
    # for i in range(len(final)):
    #     for j in range(i+1,len(final)):
    #         if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
    #             answer.discard(final[j])
    # return len(answer)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
# result: 2