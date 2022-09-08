a, b = input().split()
a, b = bool(int(a)), bool(int(b))
# print((a and (not b)) or ((not a) and b))
print(a != b)
# if a == (not b):
#     print(bool(1))
# else:
#     print(bool(0))