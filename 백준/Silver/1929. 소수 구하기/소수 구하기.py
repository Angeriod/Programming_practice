M,N=map(int, input().split())

lst=[False,False]+[True for i in range(N-1)]
N_sqrt=int(N**0.5)

for i in range(2, N_sqrt+1):
    if lst[i]==True:
        for j in range(i + i,N + 1,i):
            lst[j] = False
            
for k in range(M,N+1):
    if lst[k]==True:
        print(k)