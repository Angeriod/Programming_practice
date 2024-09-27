import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
inDegree = [0] *(N+1)

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    inDegree[b] += 1

dq = deque()
result = []

for i in range(1,N+1):
    if inDegree[i] == 0 :
        dq.append(i)

while dq:
    cur_node = dq.popleft()
    result.append(cur_node)

    for next_node in graph[cur_node]:
        inDegree[next_node] -= 1
        if inDegree[next_node] == 0:
            dq.append(next_node)

print(*result)