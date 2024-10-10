import sys

sys.setrecursionlimit(250000)

M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < M and 0 <= ny < N and matrix[x][y] > matrix[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))