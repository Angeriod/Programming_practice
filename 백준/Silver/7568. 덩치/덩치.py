N=int(input())
lst=[]
for _ in range(N):
    K,M=map(int, input().split())
    lst.append((K,M))

comp=[1]*len(lst)
for i in range(len(lst)):
    for n in range(len(lst)):
        if i==n:
            continue
        elif lst[i][0]<lst[n][0] and lst[i][1]<lst[n][1]:
            comp[i]+=1
            
print(' '.join(list(map(str, comp))))