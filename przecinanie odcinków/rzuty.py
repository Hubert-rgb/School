def det(xA, yA, xB, yB, xC, yC):
    det = xA * yB + xB * yC + xC * yA - xB * yA - xC * yB - xA * yC
    return det
def sign(i):
    if i < 0:
        return -1
    elif i > 0:
        return 1
    else:
        return 0
def cross(xA, yA, xB, yB, xC, yC, xD, yD):
    detABC = det(xA, yA, xB, yB, xC, yC)
    detABD = det(xA, yA, xB, yB, xD, yD)
    detCDA = det(xC, yC, xD, yD, xA, yA)
    detCDB = det(xC, yC, xD, yD, xB, yB)

    if detABD == 0 or detCDA == 0 or detCDB == 0 or detABC == 0:
        if detABC == 0:
            if min(xA, xB) <= xC <= max(xA, xB) and min(yA, yB) <= yC <= max(yA, yB):
                return True
        elif detABD == 0:
            if min(xA, xB) <= xD <= max(xA, xB) and min(yA, yB) <= yD <= max(yA, yB):
                return True
        elif detCDA == 0:
            if min(xC, xD) <= xA <= max(xC, xD) and min(yC, yD) <= yA <= max(yC, yD):
                return True
        elif detCDB == 0:
            if min(xC, xD) <= xB <= max(xC, xD) and min(yC, yD) <= yB <= max(yC, yD):
                return True
    else:
        if sign(detABD) != sign(detABC) and sign(detCDA) != sign(detCDB):
            return True
        else:
            return False
def length(t):
    xA = t[0]
    yA = t[1]
    xB = t[2]
    yB = t[3]
    xLength = xB - xA
    yLength = yB - yA
    length = (xLength ** 2 + yLength ** 2) ** (1/2)
    return length

dataArr = []
score = [0, 0]
for b in range(1000):
    zeroCounter = 0

    inArr = input().rstrip().split(" ")
    for h in range(len(inArr)):
        inArr[h] = int(inArr[h])
        if inArr[h] == 0:
            zeroCounter += 1
    if zeroCounter == 4:
        break
    else:
        crossArr = []
        for i in range(len(dataArr)):
            if cross(inArr[0], inArr[1], inArr[2], inArr[3], dataArr[i][0], dataArr[i][1], dataArr[i][2], dataArr[i][3]):
                currArr = [inArr[0], inArr[1], inArr[2], inArr[3], dataArr[i][0], dataArr[i][1], dataArr[i][2], dataArr[i][3], length(dataArr[i])]
                crossArr.append(currArr)
        if not crossArr:
            dataArr.append(inArr)
        else:
            crossArr.sort(key=lambda crossArr:crossArr[8], reverse=True)
            outLine = [crossArr[0][4], crossArr[0][5], crossArr[0][6], crossArr[0][7]]
            fieldLength = crossArr[0][8]
            inLength = length(inArr)
            currScore = fieldLength ** 2 + inLength ** 2

            dataArr.remove(outLine)
            if b%2 == 0:
                score[0] += currScore
            else:
                score[1] += currScore
print(int(abs(score[0] - score[1])))