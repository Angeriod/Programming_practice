import sys

N,M = map(int,sys.stdin.readline().split())
mat = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
mx = max(map(max,mat))
ans = 0
def dfs(n,sm,tlst):
    global ans
    if sm + (4-n)*mx <= ans:
        return
    if n == 4:
        ans = max(ans,sm)
        return

    for ci,cj in tlst:
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni <N and 0<= nj <M and v[ni][nj] == 0:
                v[ni][nj] = 1
                dfs(n+1,sm+mat[ni][nj],tlst+[(ni,nj)])
                v[ni][nj] = 0

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1,mat[i][j],[(i,j)])
        v[i][j] = 0

print(ans)