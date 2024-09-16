import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


coord = [[0 if i==j else float('inf') for j in range(n+1)] for i in range(n + 1) ]

for i in range(m):
    a,b,cost = map(int,sys.stdin.readline().split())
    coord[a][b] = min(cost,coord[a][b])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            coord[i][j] = min(coord[i][j], coord[i][k]+coord[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if coord[i][j] == float('inf'):
            print("0", end=" ")
        else:
            print(coord[i][j], end=" ")
    print()

