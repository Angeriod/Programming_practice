import sys

di = [-1,0,1,0]
dj = [0,1,0,-1]
def slove(ci,cj,dr):
    cnt = 0
    while 1:
        matrix[ci][cj] = 2
        cnt+=1

        flag = 1
        while flag ==1:
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
                ni,nj = ci+di[nd], cj+dj[nd]
                if matrix[ni][nj] == 0:
                    ci,cj,dr = ni,nj,nd
                    flag = 0
                    break
            else:
                bi, bj = ci - di[dr], cj - dj[dr]
                if matrix[bi][bj] == 1:
                    return cnt
                else:
                    ci, cj = bi, bj


N,M = map(int,sys.stdin.readline().split())
si, sj, dr = map(int,sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


ans = slove(si,sj,dr)
print(ans)