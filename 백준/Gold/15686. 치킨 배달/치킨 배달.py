import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

home = [(i,j) for j in range(N) for i in range(N) if matrix[i][j] == 1]
chick =[(i,j) for j in range(N) for i in range(N) if matrix[i][j] == 2]

ans = 2*N*2*N
CNT = len(chick)
def cal(tlst):
    sm = 0
    for hi,hj in home:
        mn = 2*N
        for ci,cj in tlst:
            mn = min(mn,abs(hi-ci)+abs(hj-cj))
        sm += mn

    return sm

def dfs(n,tlst):
    global ans
    if n == CNT:
        if len(tlst)==M:
            ans = min(ans, cal(tlst))
        return

    dfs(n+1,tlst+[chick[n]])
    dfs(n+1,tlst)

dfs(0,[])
print(ans)