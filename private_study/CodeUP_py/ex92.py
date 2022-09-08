a = list(map(int, input().split()))
n = len(a)
d = []
for i in range(23):
    d.append(0)

for i in range(n):
    d[a[i]-1] += 1

for i in range(23):
    print(d[i], end=' ')

print(d)