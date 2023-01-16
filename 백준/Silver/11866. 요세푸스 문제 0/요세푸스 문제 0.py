N,K=map(int,input().split())
lst=[i+1 for i in range(N)]
idx=K-1
order=[]
while(True):
    trg=lst.pop(idx)
    order.append(trg)
    idx+=(K-1)
    N=len(lst)
    if N==0:
        break
    while(idx>=N):
        idx-=N

print('<',end=''),print(*order,sep=', ',end=''),print('>')