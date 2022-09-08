n = input()
n = int(n)
i = 0
s = 0
while True:
    i += 1
    s = s + i
    if s >= n:
        break
print(s)