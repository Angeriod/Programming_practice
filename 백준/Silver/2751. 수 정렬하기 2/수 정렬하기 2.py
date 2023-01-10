import sys

N=int(sys.stdin.readline())
b=[]
for i in range(N):
    a=int(sys.stdin.readline())
    b.append(a)
b.sort()
for i in b:
    print(i)