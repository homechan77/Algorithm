#리스트 컴프리헨션
##0부터 19까지의 수 중에서 홀수만을 포함하는 리스트를 만들어보자
#array = [i for i in range(20) if i % 2 == 1]
#print(array)

#일반적인 소스코드의 사용
#array = []
#for i in range(20):
#    if i % 2 == 1:
#        array.append(i)
#print(array)

##1부터 9까지의 수의 제곱 값을 포함하는 리스트
#array = [i*i for i in range(10)]
#print(array)

#n = 3
#m = 4
#array = [[0]*m]*n
#array[1][1] = 5
#print(array)

#array = [[0]*m for _ in range(n)]
#array[1][1] = 5
#print(array)