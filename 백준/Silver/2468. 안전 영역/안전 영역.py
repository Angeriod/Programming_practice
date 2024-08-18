import sys
from collections import deque
import copy

N= int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
max_value = max(max(row) for row in matrix)

def bfs(matrix_copy, start_x, start_y, visited,height):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque([(start_x, start_y)])
    cnt = 1
    matrix_copy[start_x][start_y] = 0

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= (N - 1) and 0 <= ny <= (N - 1):
                if (nx, ny) not in visited:
                    if matrix_copy[nx][ny] > height:
                        matrix_copy[nx][ny] = 0
                        visited.add((nx, ny))
                        dq.append((nx, ny))
                        cnt += 1

    return cnt


max_region = -1e9
height = 0

while height < max_value:
    matrix_copy = copy.deepcopy(matrix)
    visited = set([(0, 0)])
    group = []
    for i in range(N):
        for j in range(N):
            if matrix_copy[i][j] > height:
                cnt = bfs(matrix_copy, i, j, visited, height)
                group.append(cnt)

    height += 1

    if max_region < len(group):
        max_region = len(group)

print(max_region)



