for test_n in range(10):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]


    result=0
    for i in range(100):
        if arr[0][i]==1:
            x,y = 0,i

            while x!=99:
                x+=1
                if y > 0 and arr[x][y-1]==1:
                    while y>0 and arr[x][y-1]==1:
                        y -= 1
                elif y < 99 and arr[x][y+1]==1:
                    while y < 99 and arr[x][y+1]==1:
                        y += 1

            if arr[x][y] == 2:
                result = i
                break


    print(f'#{N} {result}')