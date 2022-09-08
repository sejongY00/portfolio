a = []

for i in range(10):
    a.append([])

for i in range(10):
    a[i] = list(map(int, input().split()))

x = 1
y = 1

while True:
    if a[x][y] == 0: # 0일 경우에 9로 변경
        a[x][y] = 9
    elif a[x][y] == 2: # 개미집 발견 시 반복문을 빠져나옴
        a[x][y] = 9
        break

    if (a[x][y+1]==1 and a[x+1][y]==1) or (x==8 and y==8) : # 더이상 진행하지 못하거나, 미로의 끝일 경우 반복문을 빠져나옴
        break

    if a[x][y+1] != 1 : # 다음칸이 1이 아닐경우 앞으로 이동
        y += 1
    elif a[x+1][y] != 1 : # 다음칸이 1이지만 아래칸이 1이 아니면 아래로 이동
        x += 1

for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()