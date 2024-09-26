import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

def bfs(start_x,start_y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    dq = deque([(start_x,start_y,0)])
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while dq:
        x,y,wall_broken = dq.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][wall_broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if matrix[nx][ny] == 0 and visited[nx][ny][wall_broken] == 0 :
                    visited[nx][ny][wall_broken] = visited[x][y][wall_broken] + 1
                    dq.append((nx,ny,wall_broken))

                if matrix[nx][ny] == 1 and wall_broken == 0:
                    visited[nx][ny][1] = visited[x][y][wall_broken] + 1
                    dq.append((nx, ny, 1))

    return -1

print(bfs(0,0))