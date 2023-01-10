def d(x):
    if x<10:
        return x+x
    elif x<100:
        return x+(x//10)+(x%10)
    elif x<1000:
        y=x%100
        return x+x//100+y//10+y%10
    else:
        y=x%1000
        z=x%100
        return x+x//1000+y//100+z//10+z%10
lst=[0]*10036
for i in range(1,10001):
    a=d(i)
    lst[a]+=1

for j in range(1,10000):
    if lst[j]==0:
        for k in range(lst[j]+1):
            print(j)