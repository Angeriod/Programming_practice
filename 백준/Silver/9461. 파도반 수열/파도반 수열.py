T=int(input())

for i in range(T):
    n=int(input())
    lst=[]
    for i in range(n+1):
        if (i+1)==1 or (i+1)==2 or (i+1)==3:
            lst.append(1)
        elif (i+1)==4 or (i+1)==5:
            lst.append(2)
        else:
            lst.append(lst[i-5]+lst[i-1])
    print(lst[n-1])