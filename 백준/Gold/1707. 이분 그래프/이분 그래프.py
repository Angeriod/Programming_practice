import sys
sys.setrecursionlimit(20000)

K = int(sys.stdin.readline())

def dfs(cur_node):
    for next_node in graph[cur_node]:
        if visited[next_node] == visited[cur_node]:
            return False
        if visited[next_node] == 0:
            visited[next_node] = 2 if visited[cur_node] == 1 else 1
            if not dfs(next_node):
                return False
    return True

for i in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]

    for j in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V + 1)
    bipartite = True

    for node in range(1, V + 1):
        if visited[node] == 0:
            visited[node] = 1
            if not dfs(node):
                bipartite = False
                break

    if bipartite:
        print("YES")
    else:
        print("NO")
