a, m, d, n = map(int, input().split())
result = a
list1 = [result]
for i in range(1, n):
    result = (result * m) + d
    print(i)
    list1.append(result)
print(list1)
print(list1[n-1])
