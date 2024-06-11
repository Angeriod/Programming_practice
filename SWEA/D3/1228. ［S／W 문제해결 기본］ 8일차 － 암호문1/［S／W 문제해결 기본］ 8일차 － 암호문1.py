for i in range(10):
    N = int(input())
    lst = list(map(int,input().split()))
    M = int(input())
    ord = list(map(str,input().split('I')))
    final_ord = [elem.strip().split() for elem in ord if elem.strip()]
    
    for in_ord in final_ord:
        ind = int(in_ord[0])
        num = in_ord[2:]
        lst[ind:ind] = num
        
    print(f'#{i+1}',*lst[:10])