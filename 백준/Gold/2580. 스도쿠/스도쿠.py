import sys

matrix = [list(map(int,sys.stdin.readline().split())) for i in range(9)]
zero_lst = [(i,j) for i in range(9) for j in range(9) if matrix[i][j] == 0]

def valid_chek(matrix, x, y, num):
    if num in matrix[x]:
        return False

    if num in [matrix[row][y] for row in range(9)]:
        return False

    sub_x = (x // 3) * 3
    sub_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if matrix[sub_x + i][sub_y + j] == num:
                return False
    return True

def dfs(n):
    if n == len(zero_lst):
        for row in matrix:
            print(*row)
        sys.exit(0)

    x, y = zero_lst[n]

    for num in range(1, 10):
        if valid_chek(matrix, x, y, num):
            matrix[x][y] = num
            dfs(n + 1)
            matrix[x][y] = 0

dfs(0)
