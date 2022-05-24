file1 = open("doZadania1.txt", "r")
inputValues = file1.read().rstrip()
inputLines = inputValues.split("\n")

sideLength = inputLines[0]
sideLength = int(sideLength)
valuesArr = []
print(sideLength)
for i in range(1, sideLength + 1):
    valuseInLine = inputLines[i].split(" ")
    valuseInLineInt = []
    for x in valuseInLine:
        x = int(x)
        valuseInLineInt.append(x)
    valuesArr.append(valuseInLineInt)
for y in range(sideLength) :
    valuesArr[y].append(0)
lastLine = []
for x in range(sideLength + 1):
    lastLine.append(0)
valuesArr.append(lastLine)

sum = valuesArr[0][0]
indexX = 0
indexY = 0
print(valuesArr)
while indexX != (sideLength) and indexY != (sideLength):
    if valuesArr[indexX + 1][indexY] > valuesArr[indexX][indexY + 1] :
        indexX += 1
    else:
        indexY += 1
    sum += valuesArr[indexX][indexY]
    print(indexX, indexY, valuesArr[indexX][indexY], sideLength-1)

print(sum)