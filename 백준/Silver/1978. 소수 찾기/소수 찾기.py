N=int(input())
a=list(map(int, input().split()))
lst=[]
for i in a:
    count=0
    if i<=1:
        continue
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0:
        lst.append(i)
print(len(lst))