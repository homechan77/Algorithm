n = int(input())
list=[]
for _ in range(n):
    input_data = input().split()
    list.append((input_data[0], int(input_data[1])))
def sort_key(data):
    return data[1]
result = sorted(list, key=sort_key)
for i in result:
    print(i[0], end = ' ')
