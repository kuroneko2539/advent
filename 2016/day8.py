import argparse
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day8input.txt", help="file containing input key")
args = parser.parse_args()

with open(args.inFile, "r") as f:
    commands = [x.strip() for x in f.readlines()]

grid = np.zeros((6,50))

for command in commands:
    split = command.split(" ")
    if split[0] == "rect":
        y, x = int(split[1].split("x")[0]), int(split[1].split("x")[1])
        grid[0:x,0:y] = 1
    if split[0] == "rotate":
        if split[1] == "row":
            row = int(split[2].split("=")[1])
            roll = int(split[-1])
            grid[row] = np.roll(grid[row], roll)
        if split[1] == "column":
            grid = np.transpose(grid)
            row = int(split[2].split("=")[1])
            roll = int(split[-1])
            grid[row] = np.roll(grid[row], roll)
            grid = np.transpose(grid)

print(np.sum(grid))
plt.imshow(grid)
plt.show()