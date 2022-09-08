a, b = input().split()
a, b = int(a), int(b)
a, b = bool(a), bool(b)

# if (a or b) == bool(0)
#     print(bool(1))
# else:
#     print(bool(0))

print(not(a or b))