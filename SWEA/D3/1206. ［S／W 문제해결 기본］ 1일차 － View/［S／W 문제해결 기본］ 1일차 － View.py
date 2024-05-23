
for j in range(10):

    N = int(input())
    biru= list(map(int, input().split()))
    case = 0
    for i in range(2, N - 2):
        biru_minor = biru[i - 2:i + 3]
        if max(biru_minor) == biru[i]:
            biru_minor.remove(biru[i])
            case += biru[i] - max(biru_minor)
        else:
            continue

    print(f'#{j + 1} {case}')