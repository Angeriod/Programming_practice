import sys
from collections import deque

N, M, x, y, K = map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
dice_or = list(map(int, sys.stdin.readline().split()))

dice = [[0]*3 for _ in range(4)]

def dice_S_N_fn(dice,dir): # origin = [dice[0][1],dice[1][1],dice[2][1],dice[3][1]]
    if dir == 3: #3 N
        return [dice[1][1],dice[2][1],dice[3][1],dice[0][1]]
    else: #4 S
        return [dice[3][1],dice[0][1],dice[1][1], dice[2][1]]

def dice_E_W_fn(dice,dir): # origin = [dice[3][1],dice[1][0],dice[1][1],dice[1][2]]
    if dir == 1:#1 E
        return [dice[1][2],dice[3][1],dice[1][0],dice[1][1]]
    else: #2 W
        return [dice[1][0],dice[1][1],dice[1][2],dice[3][1]]

def roll_S_N(dir,board_x,board_y):
    dice_S_N = dice_S_N_fn(dice,dir)
    for i in range(4):
        dice[i][1] = dice_S_N[i]

    if board[board_x][board_y] == 0:
        board[board_x][board_y] = dice[3][1]
    else:
        dice[3][1] = board[board_x][board_y]
        board[board_x][board_y] = 0
def roll_E_W(dir,board_x,board_y):
    dice_E_W = dice_E_W_fn(dice, dir)
    for i,(dx,dy) in enumerate([(3,1),(1,0),(1,1),(1,2)]):
        dice[dx][dy] = dice_E_W[i]

    if board[board_x][board_y] == 0:
        board[board_x][board_y] = dice[3][1]
    else:
        dice[3][1] = board[board_x][board_y]
        board[board_x][board_y] = 0


cnt = 0
for num in dice_or:
    if num == 1:
        y += 1
        if y >= M :
            y -= 1
            continue
        roll_E_W(num, x, y)
        print(dice[1][1])
    elif num == 2:
        y -= 1
        if y < 0:
            y += 1
            continue
        roll_E_W(num, x, y)
        print(dice[1][1])
    elif num == 3:
        x -= 1
        if x < 0:
            x += 1
            continue
        roll_S_N(num, x, y)
        print(dice[1][1])
    else:
        x += 1
        if x >= N :
            x -= 1
            continue
        roll_S_N(num, x, y)
        print(dice[1][1])