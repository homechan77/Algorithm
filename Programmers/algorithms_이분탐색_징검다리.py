# 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return
# 참고1: https://taesan94.tistory.com/154
# 참고2: https://velog.io/@cgw0519/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC


def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    
    rocks.sort()
    
    while start <= end: 
        mid = (start + end) // 2
        del_stones = 0
        pre_stone = 0
        for rock in rocks:
            if rock - pre_stone <  mid: 
                del_stones += 1 
            else:
                pre_stone = rock
             
            if del_stones > n:
                break
                    
        if del_stones > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
            
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]	
n = 2
print(solution(distance, rocks, n))
# return: 4
