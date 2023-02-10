N,M,V=map(int, input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()
    
def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered=dfs(w,discovered)
    return discovered

from collections import deque

visited=[False]*(N+1)

def bfs(start, visited):
    queue = deque([start])
    visited[start]=True
    while queue:
      v= queue.popleft()
      print(v,end=' ')
      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i]=True

print(*dfs(V))
bfs(V,visited)