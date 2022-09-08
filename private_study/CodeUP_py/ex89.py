a, r, n = map(int, input().split())
result = a
list1 = [result]
for i in range(1, n):
    result = result * r
    print(i)
    list1.append(result)
print(result)
print(list1)