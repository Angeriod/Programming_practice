import sys

N  = int(sys.stdin.readline())

dp = [[0] * 10 for i in range(N)]
dp[0] = [0]+[1] * 9

for length in range(1,N):
        dp[length][0] = dp[length - 1][1]
        dp[length][9] = dp[length - 1][8]

        for idx in range(1,9):
            dp[length][idx] = dp[length - 1][idx - 1] + dp[length - 1][idx + 1]

print(sum(dp[N-1])%1000000000)


