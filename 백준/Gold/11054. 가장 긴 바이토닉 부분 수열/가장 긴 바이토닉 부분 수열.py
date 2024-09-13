import sys

N = int(sys.stdin.readline())
A_lst = list(map(int, sys.stdin.readline().split()))
def cal(A_lst):
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if A_lst[j] < A_lst[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp
reversed_A_lst = A_lst[::-1]
up_dp = cal(A_lst)
down_dp = cal(reversed_A_lst)
down_dp.reverse()

max_len = 0
for i in range(N):
    max_len = max(max_len,up_dp[i] + down_dp[i] - 1 )

print(max_len)