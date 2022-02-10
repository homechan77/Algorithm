# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

def solution(brown, yellow):
    # brown과 yellow를 더한 값의 약수들을 구하고 'insulist'에 저장
    sumby = brown + yellow
    insulist = []
    for i in range(sumby):
        iplus = i+1
        if sumby % iplus == 0:
            insulist.append(iplus)
    
    # 'insulist'에 들어간 약수들의 갯수가 짝수인 경우와 홀수인 경우를 나누어 x(가로),세로(y) 구하기
    # 짝수인 경우 (x-2)*(y-2) = yellow 공식을 만족해야 한다
    leninsulist = (len(insulist)) // 2
    if len(insulist) % 2 == 0:
        xindex = leninsulist
        yindex = leninsulist-1
        while (insulist[xindex]-2)*(insulist[yindex]-2) != yellow:
            xindex += 1
            yindex -= 1
        x = insulist[xindex]
        y = insulist[yindex]
    else:
        x = insulist[leninsulist]
        y = insulist[leninsulist]
    
    answer = [x, y]
        
    return answer
    
brown = 50
yellow = 22
print(solution(brown, yellow))