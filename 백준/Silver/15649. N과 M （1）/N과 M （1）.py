import itertools
N,M=map(int, input().split())

num=[ i+1 for i in range(N)]
permu=list(itertools.permutations(num,M))

for j in permu:
    print(*j)