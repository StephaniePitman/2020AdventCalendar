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

    start = int(interval[0])
    end = int(interval[1])

    character = splitMessage[1][0]
    charCount = 0

    for letter in splitMessage[2]:
        if letter == character:
            charCount += 1
            if charCount > end:
                break
    
    if charCount >= start and charCount <= end:
        correctCount += 1

print("Number of correct passwords")
print(correctCount)

