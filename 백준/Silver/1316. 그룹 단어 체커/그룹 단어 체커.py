N=int(input())
count=N
for i in range(N):
    a=input()
    lst=[]
    for j in range(len(a)):
        if j>=1:
            if a[j-1]==a[j]:
                continue
        if a[j] in lst:
            if a[j-1]!=a[j]:
                N-=1
                break
        else:
            lst.append(a[j])
print(N)