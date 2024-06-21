from collections import deque
for test_n in range(10):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
 
    q = deque()
    q.append([1,1])

    def bfs():

        while q:
            a, b = q.popleft()
            arr[a][b] = 1

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if arr[nx][ny] == 3:
                    return 1

                if 0<= nx < 16 and 0 <= ny < 16 and arr[nx][ny]==0:
                    arr[nx][ny] = 1
                    q.append([nx,ny])

    print(f'#{N} {1 if bfs() else 0}')