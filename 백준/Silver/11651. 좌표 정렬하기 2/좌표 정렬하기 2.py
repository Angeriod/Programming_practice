N=int(input())
lst=[]
for i in range(N):
    lst.append(tuple(map(int, input().split())))
    
lst.sort(key=lambda x:(x[1], x[0]))
for i,j in lst:
    print(i, j)