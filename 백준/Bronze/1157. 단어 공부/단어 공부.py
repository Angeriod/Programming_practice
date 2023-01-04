a=list(map(str, input().upper()))
a1=list(set(a))
lst=[]
for i in a1:
    k=a.count(i)
    lst.append(k)
m=max(lst)
idx=[i for i,v in enumerate(lst) if v==m]#max인 idx추출
if len(idx)>=2:#중복일때는 index가 2개이상나온다
    print("?")
else:
    print(a1[idx[0]])