N=int(input())
man=list(map(int, input().split()))
man.sort()
tot=0
for i in range(len(man)):
    for j in range(i+1):
         tot+=man[j]
            
print(tot)