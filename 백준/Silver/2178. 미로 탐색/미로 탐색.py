import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
graph = [ list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

def bfs(graph,start_x,start_y,end_x,end_y):


    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(start_x,start_y,[(start_x,start_y)])])
    visited = set([(start_x,start_y)])

    while queue:
        
        x, y, path = queue.popleft()

        if x == end_x and y == end_y:
            return print(len(path))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= (N-1) and 0 <= ny <= (M-1) :
                if (nx,ny) not in visited:
                    if graph[nx][ny] == 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, path + [(nx, ny)]))

bfs(graph,0,0,N-1,M-1)
