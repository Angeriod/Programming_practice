import sys

n = int(input())
seq=list(map(int,sys.stdin.readline().split()))
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if seq[j] < seq[i] :
            dp[i]= max(dp[i],dp[j]+1)
print(max(dp))