import argparse, numpy as np, re, sys
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day20Input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    command = f.readlines()[0].strip()[1:-1]

start = [500,500]
grid = np.full((1000,1000), None)
grid[start[0],start[1]] = "."
seenStates = []

def iteratePaths(startPos, pathSpec, depth):
    global grid
    pos = startPos.copy()
    #brackEnd = 0
    for i in range(len(pathSpec)):
        #if i <= brackEnd: continue
        if pathSpec[i] == "S":
            grid[pos[0], pos[1]+1] = "-"
            pos[1] += 2
            grid[pos[0],pos[1]] = "."
        elif pathSpec[i] == "W":
            grid[pos[0]-1, pos[1]] = "|"
            pos[0] -= 2
            grid[pos[0],pos[1]] = "."
        elif pathSpec[i] == "E":
            grid[pos[0]+1, pos[1]] = "|"
            pos[0] += 2
            grid[pos[0],pos[1]] = "."
        elif pathSpec[i] == "N":
            grid[pos[0], pos[1]-1] = "-"
            pos[1] -= 2
            grid[pos[0],pos[1]] = "."
        elif pathSpec[i] == "(":
            brackCount = 0
            pipeLoc = None
            for j in range(i+1,len(pathSpec)):
                if brackCount == 0:
                    if pathSpec[j] == "|": pipeLoc = j
                if pathSpec[j] == "(":
                    brackCount += 1
                if pathSpec[j] == ")":
                    brackCount -= 1
                if brackCount == -1:
                    end = j 
                    break
            path1 = pathSpec[i+1:pipeLoc] + pathSpec[end+1:]
            path2 = pathSpec[pipeLoc+1:end] + pathSpec[end+1:]
            #if str(pos[0]) + "," + str(pos[1]) + path1 not in seenStates:
                #seenStates.append(str(pos[0]) + "," + str(pos[1]) + path1)
            iteratePaths(pos, path1, depth+1)
            #if str(pos[0]) + "," + str(pos[1]) + path2 not in seenStates:
                #seenStates.append(str(pos[0]) + "," + str(pos[1]) + path2)
            iteratePaths(pos, path2, depth+1)
            return

iteratePaths(start, command, 0)
print("Paths Made")
pos = start.copy()

def printSurround(grid, pos):
    for i in range(-5,6,1):
        for j in range(-5,6,1):
            if grid[pos[0]+i,pos[1]+j]:
                sys.stdout.write(str(grid[pos[0]+i,pos[1]+j]) + "")
            else:
                sys.stdout.write("#")
        sys.stdout.write("\n")

def displayGrid(grid):
    tempGrid = np.full_like(grid, 0, np.float)
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == ".":
                tempGrid[i,j] = 0.5
                count += 1
            if grid[i,j] == None:
                tempGrid[i,j] = 0.0
                count += 1
            if grid[i,j] == "|" or grid[i,j] == "-":
                tempGrid[i,j] = 1.0
                count += 1
    print(grid.shape[0]*grid.shape[1], count)
    plt.imshow(tempGrid)
    #plt.show()
    plt.savefig("./day20Grid.jpg")

def displayDistGrid(grid):
    tempGrid = np.full_like(grid, 0, np.float)
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == None:
                tempGrid[i,j] = 0.0
                count += 1
            if grid[i,j] == "|" or grid[i,j] == "-":
                tempGrid[i,j] = 0.0
                count += 1
            else:
                tempGrid[i,j] = grid[i,j]
                count += 1
    print(grid.shape[0]*grid.shape[1], count)
    plt.imshow(tempGrid)
    #plt.show()
    plt.savefig("./day20DistGrid.jpg")

displayGrid(grid)

tempGrid = grid.copy()
nextCheck = [pos]
currentVal = 0
tempGrid[500,500] = 0
greaterThan1000 = 0
while len(nextCheck) > 0:
    tempCheck = []
    for check in nextCheck:
        if tempGrid[check[0]+1,check[1]] == "|":
            if tempGrid[check[0]+2,check[1]] == ".":
                tempCheck.append([check[0]+2,check[1]])
                tempGrid[check[0]+2,check[1]] = currentVal + 1
                if currentVal + 1 > 999: greaterThan1000 += 1
        if tempGrid[check[0]-1,check[1]] == "|":
            if tempGrid[check[0]-2,check[1]] == ".":
                tempCheck.append([check[0]-2,check[1]])
                tempGrid[check[0]-2,check[1]] = currentVal + 1
                if currentVal + 1 > 999: greaterThan1000 += 1
        if tempGrid[check[0],check[1]+1] == "-":
            if tempGrid[check[0],check[1]+2] == ".":
                tempCheck.append([check[0],check[1]+2])
                tempGrid[check[0],check[1]+2] = currentVal + 1
                if currentVal + 1 > 999: greaterThan1000 += 1
        if tempGrid[check[0],check[1]-1] == "-":
            if tempGrid[check[0],check[1]-2] == ".":
                tempCheck.append([check[0],check[1]-2])
                tempGrid[check[0],check[1]-2] = currentVal + 1
                if currentVal + 1 > 999: greaterThan1000 += 1
        # printSurround(tempGrid, check)
        # input()
    nextCheck = tempCheck.copy()
    currentVal += 1
    print(len(nextCheck), currentVal)

displayDistGrid(tempGrid)
with open("day20Out.jpg", "w") as f:
    f.write(str(currentVal-1) + "," + str(greaterThan1000))
