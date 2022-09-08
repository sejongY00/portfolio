
def antMaze():
    a = []
    x = 0
    y = 0
    tempList = []
    while True:
        start = input('Start? (yes or no) >>> ')
        if start == 'yes':
            h = int(input('high >>> '))
            w = int(input('width >>> '))
            for i in range(h+1):
                a.append([])
                for j in range(w+1):
                    a[i].append(0)
            print('##### Draw Your Maze! #####\nRoad = 0\nWall = 1\n')
            for i in range(1, h+1):
                while True:
                    print('{} / {} line > '.format(i, h), end=' ')
                    tempList = list(map(int, input().split()))
                    if (tempList.count(0) + tempList.count(1)) == w:
                        for j in range(1, w+1):
                            a[i][j] = tempList[j-1]
                        break
                    else:
                        print('please {} numbers use only 0 or 1.\n'.format(w))
                        continue
            a[2][2] = 9
            x = 1
            for j in range(1, h+1):
                if a[x][j] == 0:
                    a[x][j] = 9
                    print(a[i][j], end=' ')
                else:
                    x = x + 1
                    print(a[i][j], end=' ')
                print()
        elif start == 'no':
            print('Bye')
            break
        else:
            continue
        print('end')

antMaze()