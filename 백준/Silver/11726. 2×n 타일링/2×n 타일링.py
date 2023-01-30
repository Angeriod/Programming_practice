n=int(input())
lst=[]
for i in range(n):
    if i==0:
        lst.append(1)
    elif i==1:
        lst.append(2)
    else:
        lst.append(lst[i-2]+lst[i-1])
print(lst[n-1]%10007) 