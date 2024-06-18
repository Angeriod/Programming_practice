inf = 100001


def bfs(si, sj, ei, ej):
    q = []
    v = [[inf] * N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[ei][ej]


T = int(input())

for i in range(T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    #arr = [[int(bit) for bit in line] for line in input().strip().split()]

    ans = bfs(0, 0, N - 1, N - 1)

    print(f'#{i + 1} {ans}')
