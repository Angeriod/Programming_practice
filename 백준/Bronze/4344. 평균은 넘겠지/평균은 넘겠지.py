num=int(input())
for i in range(num):
    a=list(map(int, input().split()))
    N=a[0]#N추출
    a.remove(a[0])#N빼주기
    avg=sum(a)/N#평균계산
    count=0
    for i in range(len(a)):
        if a[i]>avg:
            count+=1 #평균보다 높으면 +1
    print(f'{(count/N):.3%}')