for i in range(10):
    N = int(input())
    lst = list(map(int,input().split()))
    M = int(input())
    ord = list(map(str,input().split()))
    
    for idx in range(len(ord)):
       if ord[idx] == 'D':
           D_idx = int(ord[idx+1])
           D_num = int(ord[idx+2])
           del lst[D_idx:D_idx+D_num]
       elif ord[idx] == 'I':
           I_idx = int(ord[idx+1])
           I_num = int(ord[idx+2])
           I_real_number = ord[idx+2+1:idx+2+1+I_num]
           lst[I_idx:I_idx] = I_real_number
       elif ord[idx] == 'A':
           A_num = int(ord[idx+1])
           A_real_number = ord[idx+1+1:idx+1+1+A_num]
           lst.append(A_real_number)
       else:
           continue
        
    print(f'#{i+1}',*lst[:10])