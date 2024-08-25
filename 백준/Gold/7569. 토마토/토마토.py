import sys
from collections import deque

M,N,H = map(int,sys.stdin.readline().split())

matrix =[[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
start_list = [(0, x, y, z) for z in range(H) for x in range(N) for y in range(M) if matrix[z][x][y] == 1]


def bfs(matrix, start_list):
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    day = 0
    dq = deque(start_list)

    while dq:
        day, x, y, z = dq.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if matrix[nz][nx][ny] == 0:
                    matrix[nz][nx][ny] = 1
                    dq.append((day+1,nx,ny,nz))

    return day



cnt = bfs(matrix,start_list)

if any(matrix[z][x][y] == 0 for z in range(H) for x in range(N) for y in range(M)):
    print(-1)
    sys.exit(0)

print(cnt)
