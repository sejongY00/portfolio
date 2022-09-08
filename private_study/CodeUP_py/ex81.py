n = input()
n = int(n, 16)
if (n >= 10) and (n <= 16):
    for i in range(1, 16):
        result = n * i
        print("%X*%X=%X" %(n, i, result))
        print("%s * %s = %s" %(format(n, 'X'), format(i, 'X'), format(result, 'X')))
        print("{:X}*{:X}={:X}".format(n, i, result))