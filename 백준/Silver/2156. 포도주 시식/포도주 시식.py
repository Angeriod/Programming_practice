N = int(input())

grape = []
for i in range(N):
    grape.append(int(input()))

dp = [0] * 10001

dp[0] = grape[0]
if N > 1:
    dp[1] = grape[0]+grape[1]

if N > 2:
    dp[2] = max(grape[2]+grape[1], grape[2]+grape[0], dp[1])


for n in range(3,N):
    dp[n] = max(dp[n - 2] + grape[n], dp[n - 3] + grape[n - 1]+ grape[n], dp[n - 1])

print(dp[N-1])