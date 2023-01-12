2581

M=int(input())
N=int(input())
sosu=[]
for i in range(M,N+1):
    count=0
    if i>1:
        for j in range(2,i):
            if i%j==0 :
                count+=1
                break
        if count==0:
            sosu.append(i)
        
if len(sosu)>0:
    print(f'{sum(sosu)}')
    print(f'{min(sosu)}')
else:
    print("-1")
2