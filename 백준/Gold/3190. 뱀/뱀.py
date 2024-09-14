import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
app = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
L_lst = []
for i in range(L):
    X, C = sys.stdin.readline().split()
    L_lst.append((int(X), C))

# 방향: 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
current_direction = 0  # 처음에 오른쪽을 향함
time = 0
matrix = [[0] * N for _ in range(N)]  # 보드 만들기

for x, y in app:  # 사과 표시
    matrix[x - 1][y - 1] = 2
snake = deque([(0, 0)])  # 뱀의 초기 위치
matrix[0][0] = 3  # 뱀의 위치 표시

# 방향 전환 함수
def turn(direction, C):
    if C == 'L':
        direction = (direction - 1) % 4
    else:  # C == 'D'
        direction = (direction + 1) % 4
    return direction

idx = 0
while True:
    time += 1
    head_x, head_y = snake[-1]  # 현재 뱀의 머리 위치
    dx, dy = direction[current_direction]  # 이동할 방향
    nx, ny = head_x + dx, head_y + dy  # 다음 위치

    # 벽에 부딪히거나 몸에 부딪히면 게임 종료
    if nx < 0 or nx >= N or ny < 0 or ny >= N or matrix[nx][ny] == 3:
        print(time)
        break

    # 사과가 있는 경우
    if matrix[nx][ny] == 2:
        matrix[nx][ny] = 3
        snake.append((nx, ny))  # 뱀의 머리 위치를 늘림
    else:  # 사과가 없는 경우
        matrix[nx][ny] = 3
        snake.append((nx, ny))  # 머리를 늘리고
        tail_x, tail_y = snake.popleft()  # 꼬리를 줄임
        matrix[tail_x][tail_y] = 0  # 꼬리 자리 비워줌

    # 방향 전환 시간인지 확인
    if idx < L and time == L_lst[idx][0]:
        current_direction = turn(current_direction, L_lst[idx][1])
        idx += 1
