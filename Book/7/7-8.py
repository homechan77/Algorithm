#내가 짠 소스코드
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        sum_list = []
        for i in array:
            if i-mid > 0:
                sum_list.append(i-mid)
            else:
                sum_list.append(0)
        sumlist = sum(sum_list)
        if sumlist == target:
            return mid
        elif sumlist > target:
            start = mid+1
        else:
            end = mid-1

result = binary_search(array, m, 0, max(array))
print(result)

#답안 예시
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)