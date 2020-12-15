def calculateTreesHit(right,down):
    f = open('input.txt', "r")

    f.readline().strip()
    line = ""
    index = right
    treeCount = 0
    for l in range(down):
        line = f.readline().strip()
    while line:
        if line[index%len(line)] == '#':
            treeCount += 1
        index += right

        for l in range(down):
            line = f.readline().strip()
    f.close
    return treeCount

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

total = calculateTreesHit(slopes[0][0],slopes[0][1])

for slope in slopes[1:]:
    total = total * calculateTreesHit(slope[0],slope[1])

print('ANSWER:')
print(total)
