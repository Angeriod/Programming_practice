import sys
sys.setrecursionlimit(1000000)
n,m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]

def find_parents(x):
    if parent[x] != x:
        parent[x] = find_parents(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parents(a)
    b = find_parents(b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    fn, a ,b = map(int,sys.stdin.readline().split())
    if fn == 0:
        union_parent(a,b)
    else:
        if find_parents(a) == find_parents(b):
            print("YES")
        else:
            print("NO")
