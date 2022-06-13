n = int(input())
words = [input() for _ in range(n)]

newwords = list(set(words)) # 중복 제거
newwords.sort() # 사전 순으로 정렬
newwords.sort(key=lambda x: len(x)) # 길이가 짧은 순으로 정렬

for i in newwords:
    print(i)
