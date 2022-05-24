def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return 0
    else:
        return -1
def det(x1, y1, x2, y2, x3, y3):
    det = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
    return det
def cross(xA, yA, xB, yB, xC, yC, xD, yD):
    detABC = det(xA, yA, xB, yB, xC, yC)
    detABD = det(xA, yA, xB, yB, xD, yD)
    detCDA = det(xC, yC, xD, yD, xA, yA)
    detCDB = det(xC, yC, xD, yD, xB, yB)

    if detABD == 0 or detABC == 0 or detCDB == 0 or detCDA == 0:
        if detABC == 0:
            if min(xA, xB) <= xC <= max(xA, xB) and min(yA, yB) <= max(yA, yB):
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
        if sign(detABC) != sign(detABD) and sign(detCDA) != sign(detCDB):
            return True
        else:
            return False