while True:
    w, h, b = input("가로해상도, 세로해상도, 비트수를 입력해주세요.(공백으로 구분) : ").split()
    w, h, b = map(int, (w, h, b))
    w_range = (w >= 1) and (w <= 1024)
    h_range = (h >= 1) and (h <= 1024)
    b_range = (b <= 40) and ((b % 4) == 0)
    if w_range and h_range and b_range:
        size_mb = (w * h * b) / 8 / 1024 / 1024
        print("{:.2f} MB".format(size_mb))
        break
    else:
        print("다시 입력해주세요.")