ile = input().rstrip()
ile = int(ile)
inputData = []
data = [[[0,0] for i in range(ile + 1)] for j in range(ile + 1)]
#[0] = x; [1] = y
for i in range(ile*(ile+1)):
    a = input().rstrip().split(" ")
    for j in range(len(a)):
        a[j] = int(a[j])
    data[a[2]][a[3]][1] = a[4]
    inputData.append(a)
for i in range(ile*(ile+1)):
    a = input().rstrip().split(" ")
    for j in range(len(a)):
        a[j] = int(a[j])
    data[a[2]][a[3]][0] = a[4]
    inputData.append(a)
power = int(input().rstrip())

passedWay = [[0 for i in range(ile + 1)] for j in range(ile + 1)]
for y in range(ile + 1):
    passedWay[0][y] = data[0][y][1] + passedWay[0][y - 1]
for x in range(ile + 1):
    passedWay[x][0] = data[x][0][0] + passedWay[x - 1][0]

transition = [[0, 0] for i in range((ile + 1) * 2)]
l = 1
for y in range (1, ile + 1):
    for x in range(1, ile + 1):
        passedWay[x][y] = min(data[x][y][0] + passedWay[x - 1][y], data[x][y][1] + passedWay[x][y - 1])

road = []
while x != 0 and y != 0:
    xTemp = data[x][y][0]
    yTemp = data[x][y][1]
    x = xTemp
    y = yTemp
    road.append([xTemp, yTemp])
    print(xTemp)
print(passedWay)
print(transition)