num=int(input())
tot=1
count=1
start_num=0
for i in range(1,num):
    count+=1
    tot+=i
    if tot>num:
        start_num=tot-i
        break

if num==1:
    print(f'1/1')
elif num==2:
    print(f'1/2')
elif num>=3:
    if count%2==0:
        for j in range(num-start_num+1):
            answer=f'{count-j-1}/{j+1}'
        print(answer)
    elif count%2==1:#좌로 갑시다
        for j in range(num-start_num+1):
            answer=f'{j+1}/{count-j-1}'
        print(answer)  