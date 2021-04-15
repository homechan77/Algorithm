n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse = True)
first = array[0]
second = array[1]
li = []
while True:
    li.append(first)
    if len(li) % 4 == 3:
        li.append(second)
    if len(li) == m:
        break
count = 0
for i in li:
    count += i
print(count)