import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
min_val = 0
while len(heap) >= 2:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sm = a + b
    min_val += sm
    heapq.heappush(heap,sm)

print(min_val)