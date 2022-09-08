a, d, n = input().split()
a, d, n = map(int, (a,d,n))
i = 0
list1 = [a]
while True:
    i = i + 1    
    a = a + d
    list1.append(a)
    if i == (n-1):
        break
print(a)
print(list1)