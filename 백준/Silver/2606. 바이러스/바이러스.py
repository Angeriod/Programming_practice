T=int(input())
N=int(input())
graph = [[] for _ in range(T+1)] 
for _ in range(N):
    x,y = map(int,input().split()) 
    graph[x].append(y) 
    graph[y].append(x)
    
def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs(w, discovered)
    return discovered
    
print(f'{len(dfs(1))-1}')