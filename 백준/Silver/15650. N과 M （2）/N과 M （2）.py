n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        if sorted(s)!=s:
            return
        else:
            print(*s)
            return 
        
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()