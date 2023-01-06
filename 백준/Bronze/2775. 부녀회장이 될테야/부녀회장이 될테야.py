T= int(input())

for i in range(T):
    n= int(input())
    k= int(input())
    zero= [[j+1 for j in range(k)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(k):
            if j==0:
                zero[i][j]=1#1호는 1로 채우기
                continue
            zero[i][j]=0#1층1호 이후는 0으로 채우기
    for i in range(1,n+1):
        for j in range(1,k):
            zero[i][j]=zero[i-1][j]+zero[i][j-1]#n층k호=n-1층k호_n층+k-1층(0층이후,1호이후)
    print(zero[n][k-1])