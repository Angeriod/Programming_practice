a=int(input())
for i in range(a):
    count=0
    tot=0
    b=input()
    for j in range(len(b)):
        if b[j]=='X':
            count=0
        elif b[j]=='O':
            count+=1
            tot+=count
    print(tot)