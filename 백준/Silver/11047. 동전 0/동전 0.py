N,K=map(int,input().split())
N_lst=[int(input()) for i in range(N)]
N_lst.sort(reverse=True)
min_N=0
for i in N_lst:
    if i<=K:
        min_N+=K//i
        K%=i
    if K==0:
        print(min_N)
        break