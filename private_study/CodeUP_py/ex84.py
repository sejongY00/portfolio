# h = 헤르츠, b = 비트, c = 채널, s = 초
h, b, c, s = input().split()
h, b, c ,s = map(int,(h, b, c, s))

size = h * b * c * s
mb = size / 8 / 1024 / 1024

print("{:.1f} MB".format(mb))