with open("DoZadania2.txt") as R:
    fromFile = R.read()
fromFile = fromFile.split("\n")
valueAndWeight = [[0, 0]]
for i in range(1, int(fromFile[0]) + 1):
    a = fromFile[i].split(" ")
    valueAndWeight.append([int(a[0]), int(a[1])])
wartosc = [[0 for k in range(14)] for w in range(7)]
el = [[0 for k in range(14)] for w in range(7)]

for i in range(valueAndWeight[1][1], 14):
    wartosc[1][i] = i // valueAndWeight[1][1] * valueAndWeight[1][0]
    el[1][i] = 1
# 0 - wartość 1 waga
for w in range(2, 7):
    for k in range(1, 14):
        if k < valueAndWeight[w][1]:
            wartosc[w][k] = wartosc[w - 1][k]
            el[w][k] = el[w - 1][k]
        elif k == valueAndWeight[w][1]:
            if wartosc[w - 1][k] > valueAndWeight[w][0]:
                wartosc[w][k] = wartosc[w - 1][k]
                el[w][k] = el[w - 1][k]
            else:
                wartosc[w][k] = valueAndWeight[w][0]
                el[w][k] = w
        else:
            if wartosc[w - 1][k] > wartosc[w][k - valueAndWeight[w][1]] + valueAndWeight[w][0]:
                wartosc[w][k] = wartosc[w - 1][k]
                el[w][k] = el[w - 1][k]
            else:
                wartosc[w][k] = wartosc[w][k - valueAndWeight[w][1]] + valueAndWeight[w][0]
                el[w][k] = w

print("Wartość ", wartosc[6][13])
x = 13
while x > 0:
    print("Nr rzeczy ", el[6][x])
    x = x - valueAndWeight[el[6][x]][1]
