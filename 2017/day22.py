import argparse
import numpy as np
from collections import deque

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day22input.txt", help="file containing input key")
args = parser.parse_args()

## 0, 1, 2, 3 = clean, weak, infected, flag
startGrid = np.zeros((25,25))
with open(args.inFile, "r") as f:
    lines = [line.rstrip() for line in f]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                startGrid[i,j] = 2

#print(startGrid)
    

## 250,250 = mid
## startGridSize = 25,25
## startGridPlace = 238,263
grid = np.zeros(shape=(501,501))
grid[238:263,238:263] = startGrid

pos = [250,250]
## right increments, left decrements
direction = 0
directions = [(-1,0),(0,1),(1,0),(0,-1)]

infectionCaused = 0

for _ in range(10000000):
    if grid[pos[0],pos[1]] == 0:
        direction += 3
        direction = direction % 4
        grid[pos[0],pos[1]] = 1
    elif grid[pos[0],pos[1]] == 1:
        grid[pos[0],pos[1]] = 2
        infectionCaused += 1
    elif grid[pos[0],pos[1]] == 2:
        direction += 1
        direction = direction % 4
        grid[pos[0],pos[1]] = 3
    elif grid[pos[0],pos[1]] == 3:
        direction += 2
        direction = direction % 4
        grid[pos[0],pos[1]] = 0
    else:
        print("AHHH")
    pos[0] += directions[direction][0]
    pos[1] += directions[direction][1]

    if pos[0] < 0 or pos[0] > 500 or pos[1] < 0 or pos[1] > 500: 
        print("AHHH")
        break

print(infectionCaused)
print(np.count_nonzero(grid == 2))