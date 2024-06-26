from collections import deque

def bfs(a,b):
    global answer
    q = deque()
    q.append([[a,b],str(maze[a][b])])

    while q:
        a, b = q.popleft()

        if len(b) == 7:
            answer.add(b)
        else:
            for i in range(4):
                x = a[0] + dx[i]
                y = a[1] + dy[i]
                if 0 <= x < 4 and 0 <= y < 4:
                    q.append([[x,y],b + str(maze[x][y])])

T = int(input())
for test_case in range(T):
    maze = [list(map(int,input().split())) for _ in range(4)]

    answer = set()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        for j in range(4):
            bfs(i,j)

    print(f'#{test_case+1} {len(answer)}')
