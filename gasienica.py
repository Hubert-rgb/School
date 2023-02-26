text = input()

def longestString(text):
    currentLength = 1
    maximalLength = 1
    currentChar = text[0]
    longestStringChar = text[0]
    for i in range (1, len(text)):
        if text[i] == currentChar and i != len(text) - 1:
            currentLength += 1
        elif text[i] != currentChar:

            if maximalLength < currentLength:
                maximalLength = currentLength
                longestStringChar = currentChar
            currentLength = 1
            currentChar = text[i]
        elif text[i] == currentChar and i == len(text) - 1:
            currentLength += 1
            if maximalLength < currentLength:
                maximalLength = currentLength
                longestStringChar = currentChar
    outputString = ""
    for i in range(maximalLength):
        outputString = outputString + longestStringChar
    return outputString

output = longestString(text)
print(output)

