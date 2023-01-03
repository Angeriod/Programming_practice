a,b=map(str, input().split())
a=int(''.join(reversed(a)))#역변환후 int형변환
b=int(''.join(reversed(b)))
if a>b:
    print(a)
elif a<=b:
    print(b)#비교후 출력