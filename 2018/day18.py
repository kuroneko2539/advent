import argparse, numpy as np
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day18input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

grid = np.full((len(commands),len(commands[0])),".")

for i in range(len(commands)):
    for j in range(len(commands[i])):
        grid[i,j] = commands[i][j]

for p in range(1000000000):
    newGrid = np.full((len(commands),len(commands[0])),".")
    for i in range(newGrid.shape[0]):
        for j in range(newGrid.shape[1]):
            treeCount, lumberCount = 0, 0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if x == 0 and y == 0: continue
                    if i+x < 0 or i+x >= newGrid.shape[0]: continue
                    if j+y < 0 or j+y >= newGrid.shape[1]: continue
                    if grid[i+x,y+j] == "#": lumberCount += 1
                    if grid[i+x,y+j] == "|": treeCount += 1
                    if grid[i,j] == ".":
                        if treeCount >= 3:
                            newGrid[i,j] = "|"
                        else:
                            newGrid[i,j] = "."
                    if grid[i,j] == "|":
                        if lumberCount >= 3:
                            newGrid[i,j] = "#"
                        else:
                            newGrid[i,j] = "|"
                    if grid[i,j] == "#":
                        if lumberCount > 0 and treeCount > 0:
                            newGrid[i,j] = "#"
                        else:
                            newGrid[i,j] = "."
    grid = newGrid.copy()
    tree = np.count_nonzero(grid == "|")
    lumber = np.count_nonzero(grid == "#")
    print(p, tree*lumber)

tree = np.count_nonzero(grid == "|")
lumber = np.count_nonzero(grid == "#")
print(tree*lumber)