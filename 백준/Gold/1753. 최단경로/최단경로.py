import sys
import heapq

sys.setrecursionlimit(10**6)

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


INF = 10**9
cost = [INF] * (V+1)
cost[start] = 0
heap = []
heapq.heappush(heap, (0, start)) 

def dijkstra():
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)

        if cur_cost > cost[cur_node]:
            continue

        for next_node, next_cost in graph[cur_node]:
            sum_cost = next_cost + cur_cost

            if sum_cost < cost[next_node]:
                cost[next_node] = sum_cost
                heapq.heappush(heap, (sum_cost, next_node))

dijkstra()

for i in range(1, V+1):
    if cost[i] == INF:
        print("INF")
    else:
        print(cost[i])