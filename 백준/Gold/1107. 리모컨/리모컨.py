import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
button = list(map(int,sys.stdin.readline().split()))

min_val = abs(100-N)

for num in range(999999):
    num = str(num)

    for j in range(len(num)):
        if int(num[j]) in button:
            break
        elif j == len(num) - 1:
            min_val = min(min_val, len(num) + abs(int(num)-N))

print(min_val)