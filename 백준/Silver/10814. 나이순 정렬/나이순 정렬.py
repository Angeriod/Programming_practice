N=int(input())
lst=[]
for i in range(N):
    a,b=input().split()
    lst.append((int(a),i,b))
    
lst.sort()

for i in lst:
    print(f'{i[0]} {i[2]}')