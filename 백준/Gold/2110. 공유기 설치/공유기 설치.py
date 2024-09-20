import sys

N,C = map(int,sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for i in range(N)])

left = 1
right = house[-1]-house[0]
result = 0

while left <= right:
    mid = (left+right)//2
    cur_house = house[0]
    count = 1
    for i in range(1,len(house)):
        if house[i] - cur_house >= mid:
            count += 1
            cur_house = house[i]

    if count >= C:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)

