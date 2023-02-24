N, M= map(int, input().split())
Tree=[ i for i in map(int,input().split())]
start,end=1,max(Tree)
while(start<=end):
    mid=(start+end)//2
    cnt=0
    
    for i in Tree:
        if i>mid:
            cnt+=i-mid
    
    if cnt>=M:
        start=mid+1
    else:
        end=mid-1
        
print(end)