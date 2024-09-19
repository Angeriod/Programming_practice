import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이를 늘려 스택 오버플로우 방지

V, E = map(int, sys.stdin.readline().split())
graph = []
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))

graph.sort(key=lambda x: x[2])

parent = [i for i in range(V + 1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a, b, cost in graph:
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        answer += cost  # 간선의 가중치를 더해야 함
print(answer)
