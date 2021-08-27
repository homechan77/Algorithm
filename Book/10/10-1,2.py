#기본적인 서로소 집합 알고리즘 소스코드
"""
#[find]특정 원소가 속한 집합을 찾기(루트노드 반환)
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
"""

#경로 압축 기법 소스코드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#[union]두 원소가 속한 집합을 합치기(부모노드 반환)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) #노드 개수, 간선 개수 입력
parent = [0] * (v+1) #부모 테이블 초기화

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print(parent)

#find 함수 실행_루트 노드 반환
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

#union 함수 실생_부모 노드 반환
print('부모 테이블ㅣ ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')