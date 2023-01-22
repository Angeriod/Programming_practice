from collections import deque
import sys
dq=deque()
N=int(sys.stdin.readline())
for _ in range(N):
    odr,*K=sys.stdin.readline().split()
    
    if odr=='push':
        dq.append(K)
    elif odr=='pop':
        if len(dq)!=0:
            print(*dq.popleft())
        else:
            print(-1)
    elif odr=='size':
        print(len(dq))
    elif odr=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif odr=='front':
        if len(dq)!=0:
            print(*dq[0])
        else:
            print(-1)
    elif odr=='back':
        if len(dq)!=0:
            print(*dq[-1])
        else:
            print(-1)