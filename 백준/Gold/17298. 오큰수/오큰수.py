import sys

N = int(sys.stdin.readline())
A_lst = list(map(int,sys.stdin.readline().split()))

fin_lst = [-1]*N
stack = []
for i in range(N):
    while stack and A_lst[stack[-1]] < A_lst[i]:
        fin_lst[stack.pop()] = A_lst[i]
    stack.append(i)

print(*fin_lst)