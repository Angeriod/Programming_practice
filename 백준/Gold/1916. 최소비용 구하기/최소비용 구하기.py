import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b,cost))

start,end = map(int,sys.stdin.readline().split())

cost = [1e9 for i in range(N+1)]
heap =[]
cost[start] = 0
heapq.heappush(heap,[0,start])

while heap:

    cur_cost, cur_v = heapq.heappop(heap)

    if cost[cur_v] < cur_cost:
        continue

    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= cost[next_v]:
            continue

        cost[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost,next_v])

print(cost[end])