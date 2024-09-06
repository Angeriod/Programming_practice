import sys

N = int(sys.stdin.readline())

cnt = []
def dfs(n,tlst,visited):
    if n==N:
        cnt.append(tlst)
        return

    for j in range(N):
        if visited[n][j] == 0:
            safe = True
            for pos in tlst:
                x,y = pos
                if n == x or j == y or abs(n-x) == abs(j-y):
                    safe = False
                    break

            if safe:
                visited[n][j] = 1
                dfs(n+1,tlst+[(n,j)],visited)
                visited[n][j] = 0


visited = [[0]*N for _ in range(N)]
dfs(0,[],visited)
print(len(cnt))