from collections import deque
count=0
N=int(input())
for i in range(1,N+1):
    dq=deque(str(i))
    for j in range(len(dq)-1):
        a=int(dq[0])-int(dq[1])
        dq.popleft()
        dq.append(a)
        if j==(len(dq)-2):
            dq.popleft()
    if max(dq)==min(dq):
        count+=1
print(count)