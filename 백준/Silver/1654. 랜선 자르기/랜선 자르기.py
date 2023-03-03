K, N= map(int, input().split())
lensun=[int(input()) for i in range(K)]
start,end=1,max(lensun)

while start<=end:
    mid=(start+end)//2
    cnt=0
    
    for i in lensun:
        cnt+=i//mid
        
    if cnt>=N:
        start=mid+1
    else:
        end=mid-1
        
print(end)