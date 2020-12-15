f = open('input.txt', "r")

f.readline().strip()
line = f.readline().strip()
index = 3
treeCount = 0
while line:
    if line[index%len(line)] == '#':
        treeCount += 1
    index += 3

    line = f.readline().strip()
f.close

print('ANSWER:')
print(treeCount)

