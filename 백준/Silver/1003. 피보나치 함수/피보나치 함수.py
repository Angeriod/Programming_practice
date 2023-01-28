T=int(input())
for i in range(T):
    N=int(input())
    lst=[[0],[0]]
    for i in range(N+1):
        if i==0:
            lst[0]=[1,0]
        elif i==1:
            lst[1]=[0,1]
        else:
            lst[0].append(lst[0][i-1]+lst[0][i-2])
            lst[1].append(lst[1][i-1]+lst[1][i-2])
    print(lst[0][N],lst[1][N])