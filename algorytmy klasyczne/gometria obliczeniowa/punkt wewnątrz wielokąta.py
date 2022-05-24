def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return 0
    else:
        return -1


def det(x1, y1, x2, y2, x3, y3):
    det = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    return det


def cross(xA, yA, xB, yB, xC, yC, xD, yD):
    detABC = det(xA, yA, xB, yB, xC, yC)
    detABD = det(xA, yA, xB, yB, xD, yD)
    detCDA = det(xC, yC, xD, yD, xA, yA)
    detCDB = det(xC, yC, xD, yD, xB, yB)

    if detABD == 0 or detABC == 0 or detCDB == 0 or detCDA == 0:
        if detABC == 0:
            if min(xA, xB) <= xC <= max(xA, xB) and min(yA, yB) <= max(yA, yB):
                return 1
        elif detABD == 0:
            if min(xA, xB) <= xD <= max(xA, xB) and min(yA, yB) <= yD <= max(yA, yB):
                return 1
        elif detCDA == 0:
            if min(xC, xD) <= xA <= max(xC, xD) and min(yC, yD) <= yA <= max(yC, yD):
                return 1
        elif detCDB == 0:
            if min(xC, xD) <= xB <= max(xC, xD) and min(yC, yD) <= yB <= max(yC, yD):
                return 1
    else:
        if sign(detABC) != sign(detABD) and sign(detCDA) != sign(detCDB):
            return 2
        else:
            return 0
def side(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    if cross(x1, y1, x2, y2, x3, y3, x4, y4) == 0 or cross(x1, y1, x2, y2, x5, y5, x6, y6) == 0:
        return 0
    elif cross(x1, y1, x2, y2, x3, y3, x6, y6) == 2:
        return 2
    else:
        return 1
def includedPoint(xPoint, yPoint, pointRx, pointRy, apexes):
    counter = 0
    #sprawdzanie czy prosra przecina boki
    for i in range(len(apexes) - 1):
        if cross(xPoint, yPoint, pointRx, pointRy, apexes[i][0], apexes[i][1], apexes[i + 1][0], apexes[i + 1][1]) == 2:
            counter += 1
    #odcinek ostatni punkt i 1.
    if cross(xPoint, yPoint, pointRx, pointRy, apexes[len(apexes) - 1][0], apexes[len(apexes) - 1][1], apexes[0][0], apexes[0][1]) == 2:
        counter += 1
    #sprawdza czy prosta pokrywa się i z której strony przechodzi
    for i in range(1, len(apexes) - 2):
        if cross(xPoint, yPoint, pointRx, pointRy, apexes[i][0], apexes[i][1], apexes[i + 1][0], apexes[i + 1][1]) == 1:
            if side(xPoint, yPoint, pointRx, pointRy, apexes[i - 1][0], apexes[i - 1][1], apexes[i][0], apexes[i][1], apexes[i + 1][0], apexes[i + 1][1], apexes[i + 2][0], apexes[i + 2][1]) != 2:
                counter += 1
    if cross(xPoint, yPoint, pointRx, pointRy, apexes[len(apexes) - 1][0], apexes[len(apexes) - 1][1], apexes[0][0], apexes[0][1]) == 1:
        if side(xPoint, yPoint, pointRx, pointRy, apexes[len(apexes) - 2][0], apexes[len(apexes) - 2][1], apexes[len(apexes) - 1][0], apexes[len(apexes) - 1][1], apexes[0][0], apexes[0][1]) != 2:
            counter += 1
    if counter % 2 == 0:
        return False
    else:
        return True

apexCount = int(input().rstrip())
apexes = []
maxX = 0
for i in range(apexCount):
    apex = input().rstrip().split(" ")
    apex[0] = int(apex[0])
    apex[1] = int(apex[1])

    if apex[0] > maxX:
        maxX = apex[0]

    apexes.append(apex)
point = input().rstrip().split(" ")
point[0] = int(point[0])
point[1] = int(point[1])

#punkt R znaje się poza figrą
pointR = [0, 0]
pointR[0] = maxX + 1
pointR[1] = point[1]

if includedPoint(point[0], point[1], pointR[0], pointR[1], apexes):
    print("TAK")
else:
    print("NIE")