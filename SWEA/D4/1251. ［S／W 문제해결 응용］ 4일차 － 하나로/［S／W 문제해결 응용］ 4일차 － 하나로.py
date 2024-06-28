def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a, b):
    r_a = find(a)
    r_b = find(b)
    if r_a < r_b:
        root[r_b] = r_a
    else:
        root[r_a] = r_b

T = int(input())
for test_case in range(1, T + 1):  # 인덱스 1부터 시작
    N = int(input())
    is_x = list(map(int, input().split()))
    is_y = list(map(int, input().split()))
    E = float(input())

    edges = []
    for i in range(N):
        x1, y1 = is_x[i], is_y[i]
        for j in range(i + 1, N):
            x2, y2 = is_x[j], is_y[j]
            edges.append([(x1 - x2) ** 2 + (y1 - y2) ** 2, i, j])

    edges.sort()
    root = [i for i in range(N)]
    cnt = 0
    result = 0

    for i in range(len(edges)):
        if cnt == N - 1:
            break

        d, n1, n2 = edges[i]
        if find(n1) != find(n2):
            union(n1, n2)
            cnt += 1
            result += d

    print(f"#{test_case} {int(result * E + 0.5)}")