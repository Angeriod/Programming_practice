def prim_list(n):
    sieve=[True]*n
    m=int(n//2)
    for i in range(2,m):
        if sieve[i]==True:
            for j in range(2*i,n,i):
                sieve[j]=False
                
    return [i for i in range(2,n) if sieve[i]==True]
            

T=int(input())
for _ in range(T):
    n=int(input())
    half=n//2
    prim_lst=prim_list(n)
    for i in range(half,1,-1):
        if ((n-i) in prim_lst) and (i in prim_lst):
            print(f'{i} {n-i}')
            break