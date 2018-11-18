from day10 import getKnotHash
import numpy as np

#PART 1: Get number of occupied sites

knothashes = []
for i in range(128):
    knothashes.append(getKnotHash("oundnydw-{}".format(i)))

binaryRows = []
for knothash in knothashes:
    binaryRow = []
    for i in knothash:
        binaryRow.append("{0:04b}".format(int(i, 16)))
    binaryRows.append(binaryRow)

numFull = 0
binRowsAsInts = []
for binaryRow in binaryRows:
    binRowAsInt = []
    for binaryValue in binaryRow:
        numFull += binaryValue.count("1")
        for character in binaryValue:
            binRowAsInt.append(int(character))
    binRowsAsInts.append(binRowAsInt)

print(numFull)

#PART 2: Get number of regions

grid = np.zeros((128,128), dtype=np.int)

for i in range(128):
    for j in range(128):
        grid[i,j] = -1 * binRowsAsInts[i][j]

currRegion = 1

def getRegionFromPoint(point):
    global grid
    global currRegion
    i,j = point[0], point[1]

    pointsToCheck = [(i,j)]
    while len(pointsToCheck) > 0:
        newPointsToCheck = []
        for point in pointsToCheck:
            i, j = point[0], point[1]
            grid[i,j] = currRegion
            if i > 0:
                if grid[i - 1, j] == -1:
                    newPointsToCheck.append((i-1,j))
            if j > 0:
                if grid[i, j - 1] == -1:
                    newPointsToCheck.append((i,j-1))
            if i < 127:
                if grid[i + 1, j] == -1:
                    newPointsToCheck.append((i+1,j))
            if j < 127:
                if grid[i, j + 1] == -1:
                    newPointsToCheck.append((i,j+1))   
        pointsToCheck.clear()
        for point in newPointsToCheck:
            pointsToCheck.append(point)

    currRegion += 1

for i in range(128):
    for j in range(128):
        if grid[i,j] == -1:
            getRegionFromPoint((i,j))

print(grid)
print(np.amax(grid))