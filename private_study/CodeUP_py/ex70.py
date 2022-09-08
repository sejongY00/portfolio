month = input()
month = int(month)
if month <= 12:
    if (month // 3) == 1:
        print("spring")
    elif (month // 3) == 2:
        print("summer")
    elif (month // 3) == 3:
        print("fall")
    else:
        print("winter")