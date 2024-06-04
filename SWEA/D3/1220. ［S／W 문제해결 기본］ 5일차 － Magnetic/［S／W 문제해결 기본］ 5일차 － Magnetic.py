for z in range(10):
    a = int(input())
    maze = [list(map(int,input().split())) for _ in range(a)]
    
    
    count = 0
    for i in range(len(maze)):
        state = 0
        for j in range(len(maze)):
            if maze[j][i] == 1 and state == 0:
                state = 1
            elif maze[j][i] == 2 and state == 1:
                state=0
                count+=1
                
    print(f'#{z+1} {count}')