# 가사 검색(프로그래머스_60060)

##--------------------------------------------------------------------------##
# 시도1. queries 문자열의 와일드카드 문자 시작 위치 파악을 이진 탐색 알고리즘을 활용하여 알아내고자 함
# 정확성, 효율성 모두 실패
def binary_search(string, start, end, alarm):
    answer = 0
    while start <= end:
        mid = (start+end)//2
        if alarm == 'start':
            if string[mid] == '?':
                answer = mid
                start = mid+1
            else:
                end = mid-1
        else:
            if string[mid] == '?':
                answer = mid
                end = mid-1
            else:
                start = mid+1
    return answer, alarm
    
def solution(words, queries):
    result = []
    for query in queries:
        cnt = 0
        if query[0] == '?':
            indexing, pos = binary_search(query, 0, len(query)-1, 'start')
        elif query[len(query)-1] == '?':
            indexing, pos = binary_search(query, 0, len(query)-1, 'end')
        for word in words:
            if pos == 'start':
                if (len(query) == len(word)) and (word[indexing+1:] == query[indexing+1]):
                    cnt+=1
            else:
                if (len(query) == len(word)) and (word[:indexing] == query[:indexing]):
                    cnt+=1
        result.append(cnt)
    return result


# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# print(solution(words, queries))

##--------------------------------------------------------------------------##
# 시도2. 이코테 책 참조

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 각 가사 단어의 길이는 1 이상 10,000 이하
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution2(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    for q in queries:
        # 접미사 와일드카드
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        # 접두사 와일드카드
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution2(words, queries))