import re

from pkg_resources import ResolutionError


def ex1152():
    a = input().split()
    print(len(a))

def ex1157():
    a = input().upper() # 입력받은 값 모두 대문자로 변환
    aList = list(a) # 입력받은 값 리스트로 변환
    aList.sort() # 리스트 정렬
    aListSet = list(set(aList)) # 리스트 중복 값 제거
    aListSet.sort() # 중복 값 제거한 리스트 정렬
    aListNum = [] # 정렬한 문자당 입력 갯수 저장할 리스트 생성
    for i in aListSet: # 중복값 제거 + 정렬한 리스트를 i에 대입
        aListNum.append(aList.count(i)) # 항목별 갯수 세기
    maxNum = max(aListNum) # 가장 많은 값 저장
    found = aListNum.index(maxNum) # 가장 많은 값이 몇번째 항목인지 확인
    if aListNum.count(maxNum) != 1: # 가장 많은 값이 1개 가 아닐경우 '?'출력
        print('?')
    else:
        print(aListSet[found]) # 가장 많은 값을 출력

def ex1330():
    a, b = map(int, input().split())
    if a < b:
        print('<')
    elif a > b:
        print('>')
    elif a == b:
        print('==')

def ex2438():
    star = int(input())
    for i in range(1, star+1):
        print('*' * i)

def ex2475():
    serial = list(map(int, input().split()))
    certNum = 0
    for i in range(5):
        certNum = certNum + (serial[i] ** 2)
    certNum = certNum % 10
    print(certNum)


def ex2939():
    n = int(input())
    for i in range(1, 10):
        print('{} * {} = {}'.format(n, i, n*i))

def ex2741():
    n = int(input())
    for i in range(1, n+1):
        print(i)

def ex2753():
    n = int(input())
    if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
        print('1')
    else:
        print('0')

def ex9498():
    n = int(input())
    if n >= 90:
        print('A')
    elif (n >= 80) and (n < 90):
        print('B')
    elif (n >= 70) and (n < 80):
        print('C')
    elif (n >= 60) and (n < 70):
        print('D')
    else:
        print('F')

def ex1017():
    print('\\    /\\')
    print(' )  ( \')')
    print('(  /  )')
    print(' \\(__)|')

def ex10172():
    print('|\\_/|')
    print('|q p|   /}')
    print('( 0 )"""\\')
    print('|"^"`    |')
    print('||_/=\\\\__|')

def ex999():
    s = input()
    listS = list(s)
    setS = list(set(listS))
    abc = []
    result = []
    a = ord('a')
    z = ord('z')
    for i in range(a, z+1):
        abc.append(chr(i))
    for i in range(len(abc)):
        result.append(-1)
    for i in setS:
        result[abc.index(i)] = listS.index(i)
    for i in range(len(abc)):
        print(result[i], end=' ')

def ex2675():
    t = int(input())
    listR = []
    listS = []
    for i in range(t):
        r, s = input().split()
        listR.append(int(r))
        listS.append(s)
    for i in range(t):
        for j in range(len(listS[i])):
            print(listS[i][j]*listR[i], end='')
        print()

def ex2908():
    a = input().split()
    listA = list(a)
    for i in range(2):
        reverseNum = ''
        lenNum = len(listA[i])
        for j in range(lenNum):
            reverseNum = listA[i][j] + reverseNum
        listA[i] = reverseNum
    listA = list(map(int, listA))
    maxValue = max(listA)
    print(maxValue)

def ex2920():
    listA = list(map(int, input().split()))
    listB = [1, 2, 3, 4, 5, 6, 7, 8]
    listC = [8, 7, 6, 5, 4, 3, 2, 1]
    if listA == listB:
        print('ascending')
    elif listA == listC:
        print('descending')
    else:
        print('mixed')

def ex8985():
    r = int(input())
    for i in range(r):
        a = input().upper()
        result = 0
        listA = []
        combo = []
        for j in a:
            listA.append(j)
        for j in range(len(listA)):
            if listA[j] == 'O':
                combo.append(1)
                result += sum(combo)
            else:
                combo = []
        print(result)


def ex1546():
    r = int(input())
    n = map(int, input().split())
    listN = list(n)
    maxNum = max(listN)
    newNum = []
    for i in range(r):
        newNum.append((listN[i]/maxNum)*100)
    result = sum(newNum)/r

    print(result)

def ex0001():
    point2D = list(map(int, input().split()))
    x = point2D[0]
    y = point2D[1]
    w = point2D[2]
    h = point2D[3]

    if x > w//2:
        a = w - x
    else:
        a = x

    if y > h//2:
        b = h - y
    else:
        b = y

    if a > b:
        print(b)
    else:
        print(a)

def ex0002():
    run = True
    while run:
        lista = list(map(int, input().split()))
        if lista == [0,0,0]:
            break
        maxnum = max(lista)
        lista.remove(maxnum)
        a = lista[0]
        b = lista[1]
        c = maxnum
        if (c**2) == ((a**2)+(b**2)):
            print("right")
        else:
            print("wrong")  

def ex0003():
    n = int(input())
    for i in range(1, n+1):
        num = 0
        for j in str(i):
            num = num + int(j)
        sumnum = i + num
        if n == sumnum:
            print(i)
            break
        if n == i:
            print(0)


def ex2292():
    n = int(input())
    roomNum = 0
    bum = 0
    result = 0
    begin = 2
    if n == 1:
        print(roomNum+1)
    else:
        while True:
            roomNum += 1
            bum = 6 * roomNum
            end = begin + (bum-1)
            if (n >= begin) and (n <= end):
                print(roomNum+1)
                break
            else:
                begin += (bum)

def ex2798():
    n, m = map(int, input().split())
    listCard = list(map(int, input().split()))
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if listCard[i]+listCard[j]+listCard[k] > m:
                    continue
                else:
                    result = max(result, listCard[i]+listCard[j]+listCard[k])
    print(result)