kwota=int(input("Podaj kwotę do wydania ").rstrip())
inputValues=input("Podaj wartości monet, w jednym wierszu oddzielone spacją ").rstrip()
inputValues=inputValues.split(" ")
inputValues=[int(c) for c in inputValues]
inputValues.sort()
valLength = len(inputValues) - 1
ile = [0 for i in range(valLength + 1)]

while valLength >= 0 and kwota > 0:
    ileRazy = kwota // inputValues[valLength]
    if ileRazy > 0:
        kwota -= inputValues[valLength] * ileRazy
        ile[valLength] = ileRazy
    valLength -= 1

print(ile)