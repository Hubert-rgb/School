#wczytywanie danych
fileInput = open("wektory2.txt", "r")
arr = []
allData = fileInput.read().rstrip()
data = allData.split("\n")
for i in data:
    i = i.split(" ")
    arr.append([int(i[0]), int(i[1])])

#1. podpunkt
counter1 = 0
zad1Arr = []
for x in arr:
    if x[0] == 0 or x[1] == 0:
        counter1 += 1
        zad1Arr.append([x[0], x[1]])
fileWriter1 = open("wektory_wynik1.txt", "w")
for x in zad1Arr:
    fileWriter1.write(str(x[0]) + " " + str(x[1]) + "\n")
fileWriter1.write(str(counter1))
fileWriter1.close()

#2. podpunkt
lengthsWithData = []
fileWriter2 = open("wektory_wynik2.txt", "w")
for x in arr:
    length = (x[0] * x[0] + x[1] * x[1]) ** (1/2)
    length = round(length, 2)
    lengthsWithData.append([length, x[0], x[1]])
    fileWriter2.write(str(length) + "\n")
fileWriter2.close()

#3. podpunkt
lengthsWithData = sorted(lengthsWithData)
fileWriter3 = open("wektory_wynik3.txt", "w")
for x in lengthsWithData:
    fileWriter3.write(str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + "\n")
fileWriter3.close()