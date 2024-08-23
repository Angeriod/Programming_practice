import sys
from collections import deque

N = int(sys.stdin.readline())

matrix = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]
matrix_GB = [['G' if matrix[i][j]=='R' else matrix[i][j]  for j in range(len(matrix))] for i in range(len(matrix))]

def bfs(mat, start_x, start_y, sym):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    dq = deque([(start_x, start_y)])
    mat[start_x][start_y] = 1

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx =  x + dx[i]
            ny =  y + dy[i]
            if 0<= nx < N and 0<= ny < N:
                if mat[nx][ny] == sym:
                    mat[nx][ny] = 1
                    dq.append((nx,ny))


cnt_mat = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            bfs(matrix,i,j,'G')
            cnt_mat+=1
        elif matrix[i][j] == 'B':
            bfs(matrix,i,j,'B')
            cnt_mat += 1
        elif matrix[i][j] == 'R':
            bfs(matrix,i,j,'R')
            cnt_mat += 1
        else:
            continue

cnt_mat_GB = 0

for i in range(N):
    for j in range(N):
        if matrix_GB[i][j] == 'G':
            bfs(matrix_GB,i,j,'G')
            cnt_mat_GB+=1
        elif matrix_GB[i][j] == 'B':
            bfs(matrix_GB,i,j,'B')
            cnt_mat_GB+=1
        else:
            continue

print(f'{cnt_mat} {cnt_mat_GB}')