def sortByValWei(dictionary):
    return dictionary.get("Val/Wei")


def sortByWeight(dictionary):
    return dictionary.get("Weight")


capacity = 45
# wczytywanie danych
file2 = open("DoZadania2.txt", "r")
inputValues = file2.read()
inputLines = inputValues.split("\n")

inputLenght = int(inputLines[0])

dictionary = []
for i in range(1, (inputLenght + 1)):
    inputLineArr = inputLines[i].split(" ")

    line = []
    line.append(int(inputLineArr[0]))
    line.append(int(inputLineArr[1]))
    valueForWeight = line[0] / line[1]
    line.append(valueForWeight)

    dictionary.append({"Value": line[0], "Weight": line[1], "Val/Wei": line[2]})
dictionary.sort(key=sortByValWei, reverse=True)

dictionary2 = dictionary
dictionary2 = sorted(dictionary, key=sortByWeight)

# A
indexA = 0
valueCountA = 0
capacityA = capacity
while indexA < inputLenght and capacityA >= dictionary2[0].get("Weight"):
    quantity = capacityA // dictionary[indexA].get("Weight")
    valueCountA += quantity * dictionary[indexA].get("Value")
    capacityA -= quantity * dictionary[indexA].get("Weight")
    indexA += 1
print(valueCountA)

# B
indexB = 0
valueCountB = 0
capacityB = capacity
while indexB < inputLenght and capacityB >= dictionary2[0].get("Weight"):
    if (capacityB >= dictionary[indexB].get("Weight")):
        valueCountB += dictionary[indexB].get("Value")
        capacityB -= dictionary[indexB].get("Weight")
    indexB += 1
print(valueCountB)
