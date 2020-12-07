def readFile(fileName):
    f = open(fileName, "r")
    line = f.readline().strip();
    listInput = []
    while line:
        listInput.append(line)
        line = f.readline().strip()
    f.close()
    return listInput

inputList = readFile('input.txt')

#print(inputList)
correctCount = 0

for message in inputList:
    splitMessage = message.split()
    interval = splitMessage[0].split('-')

    indexOne = int(interval[0])
    indexTwo = int(interval[1])

    character = splitMessage[1][0]
    charCount = 0

    if (splitMessage[2][indexOne-1] == character and splitMessage[2][indexTwo-1] != character) or (splitMessage[2][indexOne-1] != character and splitMessage[2][indexTwo-1] == character):
        correctCount+= 1
    

print("Number of correct passwords")
print(correctCount)

