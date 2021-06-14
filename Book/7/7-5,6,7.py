#내가 짠 소스코드
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    n_list_index = 0
    while n_list_index < n:
        if n_list[n_list_index] == i:
            print('yes', end=' ')
            break
        else:
            n_list_index += 1
        if n_list_index == n-1:
            if n_list[n_list_index] != i:
                print('no', end=' ')

#이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1):
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#계수정렬
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i i x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#집합 자료형
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')