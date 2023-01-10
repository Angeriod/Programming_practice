uni=['c=','c-','dz=','d-','lj','nj','s=','z=']
a=input()
tot=0
for i in uni:
    tot+=a.count(i)
    a=a.replace(i,'.')
a=a.replace('.','')
print(f'{tot+len(a)}')