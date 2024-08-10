import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())

#dict = {N:[2*N,N-1,N+1],}

def bfs():

    dq = deque([N])
    visited = [0] * 100001

    while dq:
        current_node = dq.popleft()

        if current_node == K:
            return print(visited[current_node])

        for node in (current_node+1, current_node-1, current_node *2):
            if 0 <= node <= 100000 and not visited[node]:
                dq.append(node)
                visited[node] = visited[current_node] + 1


bfs()