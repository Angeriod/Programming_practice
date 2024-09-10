import sys

R,C = map(int,sys.stdin.readline().split())
mat = [list(map(str,sys.stdin.readline().strip())) for _ in range(R)]
al = sorted(list(set([element for sublist in mat for element in sublist])))
v = set()
cnt = -1e9
def dfs(x,y,n):
    global cnt
    cnt = max(n,cnt)

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if mat[nx][ny] not in v:
                v.add(mat[nx][ny])
                dfs(nx, ny, n + 1)
                v.remove(mat[nx][ny])

v.add(mat[0][0])
dfs(0,0,1)

print(cnt)
