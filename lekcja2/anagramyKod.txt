reader = open("anagramy.txt", "r")

allData = reader.read().rstrip()
dataLines = allData.split("\n")
readData = []
sortedData = []
sameLengthArr = []
anagramArr = []

#inputing
for x in dataLines:
    splitedData = x.split(" ")
    readData.append(splitedData)
reader.close()

#podpunkt 1
for line in readData:
    counter = 0
    for i in range(4):
        if len(line[i]) == len(line[i+1]):
            counter += 1
    if counter == 4:
        sameLengthArr.append(line)
writer1 = open("odp_1.txt", "w")
for line in sameLengthArr:
    for word in line:
        writer1.write(word + " ")
    writer1.write("\n")
writer1.close()

#podpunkt 2
for line in readData:
    currentData = []
    for word in line:
        sortedWord = sorted(word)
        currentData.append(sortedWord)
    sortedData.append(currentData)
    counter = 0
    for i in range(4):
        if currentData[i] == currentData[i+1]:
            counter +=1
    if counter == 4:
        anagramArr.append(line)
writer2 = open("odp_2.txt", "w")
for line in anagramArr:
    for word in line:
        writer2.write(word + " ")
    writer2.write("\n")
writer2.close()