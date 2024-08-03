import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

lst_copy = lst
dict = {element: i for i, element in enumerate(sorted(set(lst)))}
lst_result = [dict[x] for x in lst]
print(*lst_result)