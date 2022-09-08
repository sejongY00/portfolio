a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
d = (a if a < b else (b if b < c else c))
print(int(d))