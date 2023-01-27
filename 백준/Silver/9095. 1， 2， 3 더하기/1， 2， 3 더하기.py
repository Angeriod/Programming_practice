T=int(input())

for j in range(T):
    N=int(input())
    lst=[]
    for i in range(N+1):
        if (i+1)==1:
            lst.append(1)
        elif (i+1)==2:
            lst.append(2)
        elif (i+1)==3:
            lst.append(4)
        else:
            lst.append(lst[i-3]+lst[i-2]+lst[i-1])
    print(lst[N-1])