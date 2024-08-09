import sys
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

matrix = sorted(matrix, key = lambda x:(x[1],x[0]))

answer = 0
endPoint = 0

for newStart, newEnd in matrix:
    if endPoint <= newStart:
        answer += 1
        endPoint = newEnd

print(answer)