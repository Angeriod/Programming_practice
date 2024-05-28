for i in range(10):
    sum_list = []
    count_tr = 0
    count = int(input())
    box_2d = [list(map(int,input().split())) for _ in range(100)]
    
    for j in range(100):
        box_mid = 0
        sum_list.append(sum(box_2d[j]))
        for z in range(100):
            box_mid += box_2d[z][j]
            if j==z:
                count_tr += box_2d[z][j]
        sum_list.append(box_mid)
                
    sum_list.append(count_tr)
    print(f'#{i+1} {max(sum_list)}') 
