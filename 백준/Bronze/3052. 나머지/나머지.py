lst=[]
for i in range(10):
    a=int(input())
    lst.append(a%42)#리스트에 나머지값 저장
print(len(set(lst)))# set으로 중복값 제거후 길이반환으로 총 몇개인지 출력 