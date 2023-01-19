import sys
N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    a=[x for x in sys.stdin.readline().split()]
    if a[0]=='size':
        print(len(stack))
    elif a[0]=='push':
        if int(a[1])>0:
            stack.append(int(a[1]))
    elif a[0]=='empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif a[0]=='top':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
    elif a[0]=='pop':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    