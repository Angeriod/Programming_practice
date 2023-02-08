n=int(input())
lst=[]
for i in range(n+1):
    if i==0:
        lst.append(1)
        continue

    if (i+1)%2==1:
        lst.append((lst[i-1]*2)-1)
    elif (i+1)%2==0: 
        lst.append((lst[i-1]*2)+1)

print(lst[n-1]%10007)