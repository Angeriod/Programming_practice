import sys

N  = int(sys.stdin.readline())
grape = [0]+[ int(sys.stdin.readline()) for _ in range(1,N+1)]

dp = [0] * 10001
dp[1] = grape[1]

if N > 1:
    dp[2] = grape[1] + grape[2]
if N > 2:
    dp[3] = max(grape[2]+grape[3],grape[1]+grape[3],grape[1]+grape[2])

#dp[4] = max(grape[2]+grape[3],grape[1]+grape[3]+grape[4],grape[1]+grape[2]+grape[4])
#dp[5] = max(grape[2]+grape[3]+grape[5],dp[1]+grape[3]+grape[4],dp[1]+grape[2]+grape[4])

for n in range(4,N+1):
    dp[n] = max(dp[n - 2] + grape[n], dp[n - 3] + grape[n - 1]+ grape[n], dp[n - 1])

print(dp[N])