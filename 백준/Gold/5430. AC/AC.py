import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = list(map(str, sys.stdin.readline().strip()))
    n = int(sys.stdin.readline())
    n_lst = deque(sys.stdin.readline().strip()[1:-1].split(','))


    flag = 0

    if n == 0:
        n_lst = []

    for fn in p:
        if fn == 'R':
            flag += 1
        elif fn == 'D':
            if len(n_lst) == 0:
                print("error")
                break
            else:
                if flag % 2 == 1:
                    n_lst.pop()
                else:
                    n_lst.popleft()
    else:
        if flag % 2 == 1:
            n_lst.reverse()
        print('['+','.join(n_lst)+']')




