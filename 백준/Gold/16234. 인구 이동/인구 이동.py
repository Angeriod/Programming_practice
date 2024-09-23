import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, visited):
    dq = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    union = [(start_x, start_y)]
    total_population = matrix[start_x][start_y]

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(matrix[x][y] - matrix[nx][ny]) <= R:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    union.append((nx, ny))
                    total_population += matrix[nx][ny]

    if len(union) > 1:
        new_population = total_population // len(union)
        for i, j in union:
            matrix[i][j] = new_population
        return True
    return False

cnt = 0
while True:
    movement = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    movement = True
    if not movement:
        break
    cnt += 1

print(cnt)
