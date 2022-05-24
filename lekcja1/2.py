arr = []
for i in range(3):
    nazwa = input()
    rok = input()
    kolor = input()
    arr.append([nazwa, rok, kolor])
sortedArr = sorted(arr, reverse=True, key = lambda arr : arr[1])
print(sortedArr)

file = open("Odpowiedz2.txt", "a")
for i in range(3):
    for j in range(3):
        file.write(sortedArr[i][j] + " ")
    file.write("\n")
file.close()