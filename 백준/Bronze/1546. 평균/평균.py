N=int(input())
a=list(map(int,input().split()))
M=max(a)
for i in range(len(a)):#담엔 for문리스트로 계산하자
    a[i]=(a[i]/M)*100
print(sum(a)/N)#평균계산