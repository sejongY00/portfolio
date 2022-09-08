from functools import reduce


a = list(map(lambda x: x ** 2, range(5)))

b = reduce(lambda x, y: y + x, 'abcde')

print(a)
print(b)