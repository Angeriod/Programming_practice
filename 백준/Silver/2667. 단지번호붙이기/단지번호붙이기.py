import sys
from collections import deque
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]


def bfs(matrix, start_x, start_y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque([(start_x, start_y)])
    cnt = 1
    matrix[start_x][start_y] = 0

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= (N - 1) and 0 <= ny <= (N - 1):
                if (nx, ny) not in visited:
                    if matrix[nx][ny] == 1:
                        matrix[nx][ny] = 0
                        visited.add((nx, ny))
                        dq.append((nx, ny))
                        cnt += 1

    return cnt

group = []
visited = set([(0, 0)])

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            cnt = bfs(matrix, i, j, visited)
            group.append(cnt)
            
group.sort()
output = str(len(group)) + '\n'
for num in group:
    output += str(num) + '\n'
print(output)