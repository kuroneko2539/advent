import argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day6input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

coords = []
maxX = 0
maxY = 0
minX = 100000
minY = 100000
for command in commands:
    x, y = int(command.split(",")[0]), int(command.split(",")[1])
    coords.append([x,y])
    if x > maxX: maxX = x
    if y > maxY: maxY = y
    if x < minX: minX = x
    if y < minY: minY = y

grid = np.zeros((maxX+1,maxY+1))
for i in range(len(coords)):
    grid[coords[i][0],coords[i][1]] = i

print(minX, maxX)

part1 = False

if part1:
    newGrid = grid.copy()
    for x in range(minX-1, maxX+1):
        for y in range(minY-1, maxY+1):
            if grid[x,y] == 0:
                minDist = 100000
                valCount = 0
                minVal = 0
                for i in range(len(coords)):
                    dist = abs(coords[i][0] - x) + abs(coords[i][1] - y)
                    if dist < minDist:
                        minDist = dist
                        valCount = 1
                        minVal = abs(i)
                    elif dist == minDist:
                        valCount += 1
                if valCount == 1:
                    newGrid[x,y] = minVal
                else:
                    newGrid[x,y] = -1

    forbiddenVals = []
    for i in range(0, maxX+1):
        val = newGrid[i,minY+2]
        if val not in forbiddenVals: forbiddenVals.append(val)
        val = newGrid[i,maxY-2]
        if val not in forbiddenVals: forbiddenVals.append(val)

    for i in range(0, maxY+1):
        val = newGrid[minX+2,i]
        if val not in forbiddenVals: forbiddenVals.append(val)
        val = newGrid[maxX-2,i]
        if val not in forbiddenVals: forbiddenVals.append(val)

    for val in forbiddenVals:
        newGrid[newGrid == val] = 0

    for i in range(len(coords)):
        unique, counts = np.unique(newGrid, return_counts=True)
        
    print(counts)
    print(max(counts[1:]))
else:
    points = 0
    for i in range(0,maxX+1):
        for j in range(0,maxY+1):
            dist = 0
            for k in coords:
                dist += abs(i-k[0]) + abs(j-k[1])
            if dist < 10000:
                points += 1
    print(points)