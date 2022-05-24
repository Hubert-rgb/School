with open("DoZadania2.txt") as R:
    d = R.read()
d = d.split("\n")
r = [[0, 0]]
for i in range(1, int(d[0]) + 1):
    a = d[i].split(" ")
    r.append([int(a[0]), int(a[1])])
wartosc = [[0 for k in range(14)] for w in range(7)]
el = [[0 for k in range(14)] for w in range(7)]

for i in range(r[1][1], 14):
    wartosc[1][i] = r[1][0]
    el[1][i] = 1
# 0 - wartość 1 waga
for w in range(2, 7):
    for k in range(1, 14):
        if k < r[w][1]:
            wartosc[w][k] = wartosc[w - 1][k]
            el[w][k] = 0
        elif k == r[w][1]:
            if wartosc[w - 1][k] > r[w][0]:
                wartosc[w][k] = wartosc[w - 1][k]
                el[w][k] = 0
            else:
                wartosc[w][k] = r[w][0]
                el[w][k] = 1
        else:
            if wartosc[w - 1][k] > wartosc[w - 1][k - r[w][1]] + r[w][0]:
                wartosc[w][k] = wartosc[w - 1][k]
                el[w][k] = 0
            else:
                wartosc[w][k] = wartosc[w - 1][k - r[w][1]] + r[w][0]
                el[w][k] = 1

print("Wartość ", wartosc[6][13])
k = 13
w = 6
while k > 0 and w > 0:
    while el[w][k] != 1:
        w -= 1
    if w > 0:
        print("Nr rzeczy ", w)
    k = k - r[w][1]
    w -= 1
