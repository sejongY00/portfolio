n = list(map(int, input().split()))
k = len(n)

for i in range(k-1, -1, -1):
    print(n[i], end=' ')
print(n)