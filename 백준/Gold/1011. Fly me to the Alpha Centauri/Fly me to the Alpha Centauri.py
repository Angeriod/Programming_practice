import sys

T = int(sys.stdin.readline())
y_x = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]

for i in range(T):
    x,y = y_x[i]

    distance = y-x
    cnt = 0
    move = 1
    move_plus = 0

    while move_plus<distance:
        cnt += 1
        move_plus += move
        if cnt % 2 == 0:
            move += 1

    print(cnt)