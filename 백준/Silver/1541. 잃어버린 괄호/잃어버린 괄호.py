a=input()
b=a.split('-')
num=0
temp=0
count=1
for i in b:
    c=i.split('+')
    
    for j in c:
        if count==1:
            num+=int(j)
        else:
            temp+=int(j)
    count=0
print(num-temp)