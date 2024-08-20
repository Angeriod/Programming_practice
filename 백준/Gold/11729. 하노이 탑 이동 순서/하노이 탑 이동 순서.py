import sys

N = int(sys.stdin.readline())

def hanoi(num, from_, to, other):
    if num ==0:
        return
    hanoi(num-1, from_, other, to)# 1 2 3, 1->2로
    print(from_, to)#1->3 으로 N짜리 옮기기
    hanoi(num-1, other,to,from_)# 2 3 1, 2->3로

print(2**N - 1)
hanoi(N,1,3,2)
