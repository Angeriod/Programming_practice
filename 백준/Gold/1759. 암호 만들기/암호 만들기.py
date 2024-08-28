import sys

L,C = map(int,sys.stdin.readline().split())
code = sorted(list(map(str,sys.stdin.readline().split())))
vow = {'a','e','i','o','u'}

ans = []
def dfs(n,prev,a_lst):
    if n == L:
        vow_count = sum(1 for sub in a_lst if sub in vow)
        cons_count = L - vow_count
        
        if vow_count >= 1 and cons_count >= 2:
            ans.append(a_lst)
        return

    for i in range(prev,C):
        dfs(n+1,i+1,a_lst+[code[i]])

dfs(0,0,[])


print( '\n'.join(''.join(sub) for sub in ans))



