import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

virus = [(i, j) for i in range(N) for j in range(M) if matrix[i][j] == 2]
wall_lst = []

def bfs(matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque(virus)

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                dq.append((nx, ny))

def dfs(n, arr):
    if n == 3:
        matrix_copy = copy.deepcopy(arr)
        bfs(matrix_copy)

        safe_area = sum(row.count(0) for row in matrix_copy)
        wall_lst.append(safe_area)
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(n + 1, arr)
                arr[i][j] = 0

dfs(0, matrix)
print(max(wall_lst))