def solution(phone_book):
    # 효율성 테스트 실패
    # phonebook = [list(i) for i in phone_book]
    # for j in phonebook:
    #     for k in phonebook:
    #         if j == k:
    #             continue
    #         n = len(j)
    #         if k[:n] == j:
    #             return False
    
    phone_book.sort()
    
    # phone_book 리스트를 정렬함으로서 인접한 앞 뒤 요소만 비교
    for i in enumerate(phone_book):
        if i[0] == 0:
            if i[1] == phone_book[i[0]+1][:len(i[1])]:
                return False
        if i[0] == len(phone_book)-1:
            if i[1] == phone_book[i[0]-1][:len(i[1])]:
                return False
            else:
                continue
        if i[1] == phone_book[i[0]+1][:len(i[1])]:
            return False
        if i[1] == phone_book[i[0]-1][:len(i[1])]:
            return False
            
    return True
    
phone_book = ["123","456","789"]
print(solution(phone_book))