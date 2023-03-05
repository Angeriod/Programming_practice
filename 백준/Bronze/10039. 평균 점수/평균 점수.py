a=[int(input()) for i in range(5)]
for i in range(5):
    if a[i]<40:
        a[i]+=40-a[i]
print(int(sum(a)/len(a)))