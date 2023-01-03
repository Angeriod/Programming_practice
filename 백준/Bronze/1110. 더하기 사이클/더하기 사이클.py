num=int(input())
ori=num
count=0
while(True):
    count+=1
    a=num//10
    b=num%10
    c=(a+b)%10
    num=int(str(b)+str(c))#하나씩 분해해서 더하기
    if num==ori:
        print(count)
        break