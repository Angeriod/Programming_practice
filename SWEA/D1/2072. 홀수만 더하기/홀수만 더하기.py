a = int(input())
for j in range(a):
    sum = 0
    lst= list(map(int, input().split()))
    for i in lst:
        if i%2==1:
            sum+=i
            
    print(f'#{j+1} {sum}')      