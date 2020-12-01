def readFile(fileName):
    f = open(fileName, "r")

    line = f.readline().strip();
    listInput = []
    while line:
        listInput.append(int(line))
        line = f.readline().strip()
    f.close
    return listInput

def findSumOf3(listInput):
    total = 0

    for x in listInput:
        for y in listInput:
            for z in listInput:
                if x + y + z == 2020:
                    return x * y * z
    return -1

listInput = readFile('input.txt')
total = findSumOf3(listInput)

if(total > 0):
    print(total)
else:
    print("no three integers summed to 3")