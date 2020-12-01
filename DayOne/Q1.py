
def readFile(fileName):
    f = open(fileName, "r")
    line = f.readline().strip();
    listInput = []
    while line:
        listInput.append(line)
        line = f.readline().strip()
    f.close()
    return listInput

def createDictionary(listInput):
    inputDictionary = {}

    for val in listInput:
        if val != '':
            if val in inputDictionary :
                inputDictionary[val] += inputDictionary[val] + 1
            else:
                inputDictionary[val] = 1
    return inputDictionary
    
def getProductOfSum(inputDictionary):
    total = 0
    for val in inputDictionary:
        if str(2020 - int(val)) in inputDictionary:
            return int(val) * int(2020-int(val))
    return -1

listInput = readFile('input.txt')
inputDictionary = createDictionary(listInput)
total = getProductOfSum(inputDictionary)

if(total == -1):
    print("no pair found to sum to 2020")
else:
    print(total)

        
