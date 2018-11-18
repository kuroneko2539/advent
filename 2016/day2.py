import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day2input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    movements = [x.strip() for x in f.readlines()]

grid = np.arange(1,10,dtype=np.int)
grid = grid.reshape((3,3))

pos = [1,1]

for movement in movements:
    for step in movement:
        if step == "U":
            if pos[0] != 0:
                pos[0] -= 1
        elif step == "R":
            if pos[1] != 2:
                pos[1] += 1
        elif step == "D":
            if pos[0] != 2:
                pos[0] += 1
        elif step == "L":
            if pos[1] != 0:
                pos[1] -= 1
    print(grid[pos[0],pos[1]])

print()

grid = np.empty((5,5), dtype=str)
grid[0] = [None,None,"1",None,None]
grid[1] = [None,"2","3","4",None]
grid[2] = ["5","6","7","8","9"]
grid[3] = [None,"A","B","C",None]
grid[4] = [None,None,"D",None,None]

pos = [2,0]

for movement in movements:
    for step in movement:
        if step == "U":
            if pos[0] != 0:
                pos[0] -= 1
                if grid[pos[0],[pos[1]]] == "N":
                    pos[0] += 1
        elif step == "R":
            if pos[1] != 4:
                pos[1] += 1
                if grid[pos[0],[pos[1]]] == "N":
                    pos[1] -= 1
        elif step == "D":
            if pos[0] != 4:
                pos[0] += 1
                if grid[pos[0],[pos[1]]] == "N":
                    pos[0] -= 1
        elif step == "L":
            if pos[1] != 0:
                pos[1] -= 1
                if grid[pos[0],[pos[1]]] == "N":
                    pos[1] += 1
    print(grid[pos[0],pos[1]])