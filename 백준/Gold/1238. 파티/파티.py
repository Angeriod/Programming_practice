import sys
import heapq

N,M,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for i in range(M):
    s,e,T = map(int,sys.stdin.readline().split())
    graph[s].append((T,e))
    reverse_graph[e].append((T,s))

def dijkstra(start,graph,N):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    heap = [(0,start)]

    while heap:

        cur_dist, cur_node = heapq.heappop(heap)

        if cur_dist > dist[cur_node]:
            continue

        for next_dist, next_node in graph[cur_node]:
            sum_cost = cur_dist + next_dist
            if sum_cost < dist[next_node]:
                dist[next_node] = sum_cost
                heapq.heappush(heap,(sum_cost,next_node))

    return dist

to_X = dijkstra(X, reverse_graph, N)
from_X = dijkstra(X, graph, N)

max_time = 0
for i in range(1,N+1):
    total_time = to_X[i] + from_X[i]
    max_time = max(max_time, total_time)

print(max_time)


