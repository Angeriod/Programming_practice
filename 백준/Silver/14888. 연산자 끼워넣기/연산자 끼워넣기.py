import sys

N= int(sys.stdin.readline())
A_list = list(map(int,sys.stdin.readline().split()))
otr = list(map(int,sys.stdin.readline().split()))

mx = -1e9
mn = 1e9

def dfs(depth,total):
    global mx,mn

    if depth == N-1:
        mx = max(total,mx)
        mn = min(total,mn)
        return

    if otr[0] != 0:
        otr[0] -= 1
        dfs(depth + 1, total + A_list[depth+1] )
        otr[0] += 1

    if otr[1] != 0:
        otr[1] -= 1
        dfs(depth + 1, total - A_list[depth+1])
        otr[1] += 1

    if otr[2] != 0:
        otr[2] -= 1
        dfs(depth + 1, total * A_list[depth+1])
        otr[2] += 1

    if otr[3] != 0:
        otr[3] -= 1
        dfs(depth + 1, int(total / A_list[depth+1]))
        otr[3] += 1

dfs(0, A_list[0])
print(mx)
print(mn)