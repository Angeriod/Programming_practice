import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,cost = map(int,sys.stdin.readline().split())
    graph[a].append((b,cost))


coord = [[0] * (n + 1) for i in range(n + 1)]
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    cost = [float('inf')] * (n + 1)
    cost[start] = 0
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)

        if cur_cost > cost[cur_node]:
            continue

        for next_node,next_cost in graph[cur_node]:
            sum_cost = cur_cost + next_cost

            if sum_cost < cost[next_node]:
                cost[next_node] = sum_cost
                heapq.heappush(heap, (sum_cost, next_node))

    return cost

for i in range(1,n+1):
    min_costs = dijkstra(i)
    for j in range(1,n+1):
        if min_costs[j] == float('inf'):
            coord[i][j] = 0
        else:
            coord[i][j] = min_costs[j]

for i in range(1, n + 1):
    print(' '.join(map(str, coord[i][1:])))