n = int(input())
nlist = sorted(list(map(int, input().split())))
m = int(input())
mlist = list(map(int, input().split()))


def binary_search(target, nlist, start, end):
    mid = (start+end) // 2

    if start > end:
        return 0

    if nlist[mid] == target:
        return 1
    elif target < nlist[mid]:
        end = mid-1
        return binary_search(target, nlist, start, end)
    else:
        start = mid+1
        return binary_search(target, nlist, start, end)

for i in mlist:
    start = 0
    end = n-1
    print(binary_search(i, nlist, start, end))
