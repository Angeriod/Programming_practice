import sys
from collections import deque
N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start_point):
    dq = deque()
    dq.append(start_point)

    node_finder = [0] * (N + 1)
    while dq:
        node = dq.pop()

        for element in graph[node]:

            if node_finder[element] == 0:
                node_finder[element]= node
                dq.append(element)



    return node_finder[2:]

a = dfs(graph,1)

[print(i) for i in a]
