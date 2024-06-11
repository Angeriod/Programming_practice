for i in range(10):
    a = int(input())
    lst = list(map(int,input().split()))
    thres = 1
 
    while(1):
        if thres % 6 == 0:
            thres = 1
        ins = lst.pop(0)
        red = ins - thres
        if red > 0:
            lst.append(red)
            thres+=1
        else:
            lst.append(0)
            break
    
    print(f"#{i+1} ",*lst)