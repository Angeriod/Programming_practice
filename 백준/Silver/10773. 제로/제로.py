import sys
K=int(sys.stdin.readline())
stack=[]
for i in range(K):
    a=int(sys.stdin.readline())
    if a==0 and len(stack)!=0:
        stack.pop()
    elif a!=0:
        stack.append(a)
print(sum(stack))