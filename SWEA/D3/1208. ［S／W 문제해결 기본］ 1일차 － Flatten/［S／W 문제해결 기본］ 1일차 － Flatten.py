for i in range(10):
    count = int(input())
    heights = list(map(int, input().split()))
    
    for _ in range(count):
        maxi = max(heights)
        mini = min(heights)
        
        maxi_index = heights.index(maxi)
        mini_index = heights.index(mini)
        
        heights[maxi_index]-=1
        heights[mini_index]+=1
        
    print(f'#{i+1} {max(heights)-min(heights)}')