import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
ripe_tomato =[(0, i, j) for i in range(N) for j in range(M) if matrix[i][j] == 1]

def bfs(matrix, ripe_tomato):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    day = 0
    dq = deque(ripe_tomato)
    while dq:
        day, x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = 1
                    dq.append((day+1,nx,ny))

    return day

if not ripe_tomato:
    print(-1)
    sys.exit(0)
    
day = bfs(matrix,ripe_tomato)

for row in matrix:
    if 0 in row:
        print(-1)
        sys.exit(0)

print(day)
