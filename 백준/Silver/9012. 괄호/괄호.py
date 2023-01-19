N=int(input())
for i in range(N):
    a=input()
    stack=[]
    
    for j in a:
        if j=='(':
            stack.append(j)
        elif j==')':
            if len(stack)==0:
                stack.append(j)
                break
            else:
                stack.pop()
    if len(stack)!=0:
        print("NO")
    else:
        print("YES")