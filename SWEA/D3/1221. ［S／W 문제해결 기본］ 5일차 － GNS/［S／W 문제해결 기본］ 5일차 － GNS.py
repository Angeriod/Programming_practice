case_dic = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
a = int(input())
for i in range(a):
    _,len_case = input().split()
    test_case = list(map(str,input().split()))
    sort_lst = []
    for j in test_case:
        sort_lst.append(case_dic[j])
    sort_lst=sorted(sort_lst)
    keys_replaced = [k for v in sort_lst for k, val in case_dic.items() if val == v]
    
    print(f'#{i+1}')
    print(*keys_replaced)