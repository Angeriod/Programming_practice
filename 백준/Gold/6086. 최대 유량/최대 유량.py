import sys
from collections import deque

N = int(sys.stdin.readline())
capacity = [[0]*52 for _ in range(52)]
def char_to_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') # 0 ~ 25
    return ord(c) - ord('a') + 26 # 26 ~ 51

def bfs(capacity, flow, source, sink, parent):
    q = deque([source])
    visited = [-1] * 52
    visited[source] = source

    while q:
        cur = q.popleft()
        if cur == sink:
            return True

        for nxt in range(52):
            if capacity[cur][nxt] - flow[cur][nxt] > 0 and visited[nxt] == -1: # 유랑이 남아있고 안가봤을 경우
                visited[nxt] = cur
                parent[nxt] = cur
                q.append(nxt)

    return False

def edmonds_karp(capacity, source, sink):
    flow = [[0]*52 for _ in range(52)]
    total_flow = 0
    parent = [-1] * 52

    while bfs(capacity,flow,source,sink,parent):
        max_flow = float('inf')
        idx = sink
        while idx != source:
            max_flow = min(max_flow, capacity[parent[idx]][idx] - flow[parent[idx]][idx])
            idx = parent[idx]

        idx = sink

        while idx != source:
            flow[parent[idx]][idx] += max_flow
            flow[idx][parent[idx]] -= max_flow
            idx = parent[idx]

        total_flow += max_flow

    return total_flow

for _ in range(N):
    a,b,f = sys.stdin.readline().split()
    a_idx = char_to_index(a)
    b_idx = char_to_index(b)
    f = int(f)
    capacity[a_idx][b_idx] += f
    capacity[b_idx][a_idx] += f

source = char_to_index('A')
sink = char_to_index('Z')
print(edmonds_karp(capacity, source, sink))

