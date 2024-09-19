import sys
import heapq

V,E = map(int,sys.stdin.readline().split())
graph = [[] for i in range(V+1)]
visited = [False]*(V+1)
heap = [[0,1]]
for i in range(E):
    a,b,c, = map(int,sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

answer = 0
while heap:

    cur_cost,cur_node = heapq.heappop(heap)
    if not visited[cur_node]:
        visited[cur_node] = True
        answer += cur_cost

        for i in graph[cur_node]:
            heapq.heappush(heap,i)


print(answer)