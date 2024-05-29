for tc in range(10):
    length = int(input())
    maze = [list(input()) for _ in range(8)] # 가로를 찾을 때 사용
    t_maze = list(map(list, zip(*maze))) # 세로를 찾을 때 사용

    ans = 0
    for i in range(len(maze)):
        for j in range(len(maze)-length +1):
            a = maze[i][j:j+length]
            if a == a[::-1]:
                ans += 1

    
    for m in range(len(t_maze)):
        for n in range(len(t_maze)-length +1):
            b = t_maze[m][n:n+length]
            if b == b[::-1]:
                ans += 1

    print(f"#{tc+1} {ans}")