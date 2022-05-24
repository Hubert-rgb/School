stringArr = []
intArr = []
for i in range(100):
    inpInt, inpStr = input().rstrip().split(" ")
    inpInt = int(inpInt)
    if inpInt == len(inpStr):
        stringArr.append(inpStr)
        intArr.append(inpInt)
lowestInt = intArr[0]
lowestIntIndexArr = []
lowestIntIndexArr.append(0)
#szukanie najniższych
for i in range(1, len(stringArr)):
    if intArr[i] < lowestInt:
        lowestInt = intArr[i]
        while len(lowestIntIndexArr) != 0:
            lowestIntIndexArr.remove(lowestIntIndexArr[0])
        lowestIntIndexArr.append(i)
    elif intArr[i] == lowestInt:
        lowestIntIndexArr.append(i)
if len(lowestIntIndexArr) == 1:
    print(lowestInt, stringArr[lowestIntIndexArr[0]])
else:
    lowestStrArr = []
    for x in lowestIntIndexArr:
        a = stringArr[x]
        lowestStrArr.append(a)
    lowestStrArr = sorted(lowestStrArr)
    print(lowestInt,lowestStrArr[0])
