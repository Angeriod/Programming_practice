import sys

N, S = map(int, sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
current_sum = 0
min_length = float('inf')

while right < N:
    current_sum += n_lst[right]
    right += 1

    while current_sum >= S:
        min_length = min(min_length, right - left)
        current_sum -= n_lst[left]
        left += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)