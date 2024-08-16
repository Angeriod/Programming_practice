import sys

N= int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

def dfs(depth,idx):
    global min_val
    if depth == N//2:
        start_sum, link_sum = 0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_sum +=matrix[i][j]
                elif not visited[i] and not visited[j]:
                    link_sum +=matrix[i][j]
        min_val = min(min_val,abs(start_sum - link_sum))
        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False


visited = [False for _ in range(N)]
min_val = 1e9

dfs(0,0)
print(min_val)