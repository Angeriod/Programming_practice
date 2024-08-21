import sys

N,K = map(int,sys.stdin.readline().split())
W_V_list = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(K+1)]

for i in range(K+1):
    for j in range(1,N+1):
        if W_V_list[j - 1][0] <= i:
            dp[i][j] = max(dp[i][j-1], W_V_list[j-1][1] + dp[i - W_V_list[j-1][0]][j-1])
        else:
            dp[i][j] = dp[i][j-1]

print(dp[K][N])
