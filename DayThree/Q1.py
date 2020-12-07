def readFile(fileName):

    
    return listInput

f = open(fileName, "r")

line = f.readline().strip();
    listInput = []
    while line:
        listInput.append(int(line))
        line = f.readline().strip()
    f.close

