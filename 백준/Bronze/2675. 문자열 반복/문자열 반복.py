num=int(input())
for i in range(num):
    lst=[]
    a,b=input().split()#둘다 string으로 받음
    for j in range(len(b)):
        lst.append(b[j]*int(a))#a는 string이므로 형변환해야함
    print(''.join(lst))#lst를 하나로 합치기